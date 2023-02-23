# Algorithm that finds the max houses to be painted based on the earliest endDay of each house [OPTIMIZED TIME COMPLEXITY]

from typing import List
import heapq


class NodeObj:
    def __init__(self, startDay: int, endDay: int, index: int):
        self.startDay: int = startDay
        self.endDay: int = endDay
        self.index: int = index

    def __str__(self):
        return "StartDay: {0} | EndDay: {1} | Index: {2}".format(
            self.startDay, self.endDay, self.index
        )

    # We sort based on the earliest endDay for a given house and in case of a tie, we sort secondarily on startDay and index.
    def __lt__(self, other):
        return (
            (self.endDay < other.endDay)
            or ((self.endDay == other.endDay) and (self.startDay < other.startDay))
            or (
                (self.endDay == other.endDay)
                and (self.startDay == other.startDay)
                and (self.index < other.index)
            )
        )


# extractUniqueKeys uses the sorted order of the days to return list of unique startDays which can be used for jumping to next smallest interval
def extractUniqueKeys(days, n):
    keysSet = []
    prev = -1
    for start, _ in days:
        if start != prev:
            prev = start
            keysSet.append(start)

    return keysSet


def main(n: int, m: int, days: List[int]) -> List[int]:
    # earliestEndDayHeap consists of intervals that end the earliest
    earliestEndDayHeap: List[NodeObj] = []
    heapq.heapify(earliestEndDayHeap)

    daysIdx: int = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    # unique days of atmost length m
    keysSet = extractUniqueKeys(days, n)

    # no interval has a startDay <= n
    if (len(keysSet)) == 0:
        return []

    startDay = max(1, keysSet[0])
    keySetIdx = 0

    while startDay < n:
        # update the latest keySet index inorder to jump to the next available day when no value exists in the heap
        if keySetIdx < len(keysSet) and keysSet[keySetIdx] <= startDay:
            keySetIdx += 1

        # We store all the houses that atmost begin at currentDay
        while daysIdx < m and days[daysIdx][0] <= startDay:
            if days[daysIdx][1] >= startDay:
                heapq.heappush(
                    earliestEndDayHeap,
                    NodeObj(days[daysIdx][0], days[daysIdx][1], daysIdx),
                )
            daysIdx += 1

        # If there exists more houses to paint but we have none in our priority queue, then we just jump to the next lowest interval
        # with interval's startDay greater than current startDay. If there are no more houses to paint, then we exit the loop
        if len(earliestEndDayHeap) == 0:
            if keySetIdx == len(keysSet):
                break

            startDay = keysSet[keySetIdx]
            keySetIdx += 1

        # We then find the house with the earliest endDay that has the current day and paint it.
        while len(earliestEndDayHeap) > 0:
            node: NodeObj = heapq.heappop(earliestEndDayHeap)
            if startDay >= node.startDay and startDay <= node.endDay:
                resultIndicesArr.append(node.index + 1)
                startDay += 1
                break

    return resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*logm)
SPACE COMPLEXITY : O(m) 

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the starting houses have larger duration than the subsequent houses.
=> n = 5; m = 4; days = [(1,2), (1,3), (1,4), (2, 3)]

According to current algorithm:
1) House at index 1 is painted on day 1 => 1 lies between (1, 2)
2) House at index 2 is painted on day 2 => 2 lies between (1, 3)
3) House at index 4 is painted on day 3 => 3 lies between (2, 3)
3) House at index 3 is painted on day 4 => 4 lies between (1, 4)
Total number of houses painted = 4 (1, 2, 3, 4)

Optimal Solution:
The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
    This greedy approach always yields the optimal solution
        
"""
