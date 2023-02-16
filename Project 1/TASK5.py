# Algorithm that finds the max houses to be painted based on the earliest endDay of each house [OPTIMIZED TIME COMPLEXITY]

from typing import List
import heapq

from helpers.AVLTree import AVLTree


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


def extractUniqueKeys(days, n):
    keysSet = set()
    for start, end in days:
        if start <= n:
            keysSet.add(start)
        if end <= n:
            keysSet.add(end)

    keysSet = list(keysSet)
    keysSet.sort()
    return keysSet


def initializeAVLTree(keys):
    avlTreeObj = AVLTree()
    root = None
    for val in keys:
        root = avlTreeObj.insert(root, val)

    return avlTreeObj, root


def main(n: int, m: int, days: List[int]) -> List[int]:
    # earliestEndDayHeap consists of intervals that end the earliest
    earliestEndDayHeap: List[NodeObj] = []
    heapq.heapify(earliestEndDayHeap)

    daysIdx: int = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    # unique days of length m
    keysSet = extractUniqueKeys(days, n)
    avlTreeObj, root = initializeAVLTree(keysSet)
    startDay = keysSet[0]
    keySetIdx = 0

    while not (startDay > n or (daysIdx == m and len(earliestEndDayHeap) == 0)):
        # update the latest keySet index to jump to the next available day when no value exists in the heap
        while keySetIdx < len(keysSet) and keysSet[keySetIdx] <= startDay:
            keySetIdx += 1

        # We store all the houses that atmost begin at currentDay
        while daysIdx < m and days[daysIdx][0] <= startDay:
            if days[daysIdx][1] >= startDay:
                heapq.heappush(
                    earliestEndDayHeap,
                    NodeObj(days[daysIdx][0], days[daysIdx][1], daysIdx),
                )
            daysIdx += 1

        # We then find the earliest endDay house which includes the current day and paint it.
        if len(earliestEndDayHeap) == 0:
            if keySetIdx < len(keysSet):
                startDay = keysSet[keySetIdx]
                keySetIdx += 1

        else:
            while len(earliestEndDayHeap) > 0:
                node: NodeObj = heapq.heappop(earliestEndDayHeap)
                avlTreeObj.setInterval(node.startDay, node.endDay)
                closestStartDate = avlTreeObj.getClosestSmallestNode(root)
                if closestStartDate != 10**9 + 7:
                    resultIndicesArr.append(node.index)
                    root = avlTreeObj.removeAndInsertNext(root, closestStartDate)
                    startDay += 1
                    break

    return resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*logm)
SPACE COMPLEXITY : O(n + m) 

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the starting houses have larger duration than the subsequent houses.
=> n = 5; m = 4; days = [(1,2), (1,3), (1,4), (2, 3)]

According to current algorithm:
1) House at index 0 is painted on day 1 => 1 lies between (1, 2)
2) House at index 1 is painted on day 2 => 2 lies between (1, 3)
3) House at index 3 is painted on day 3 => 3 lies between (2, 3)
3) House at index 2 is painted on day 4 => 4 lies between (1, 4)
Total number of houses painted = 4 (0, 1, 3, 2)

Optimal Solution:
The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
    This greedy approach always yields the optimal solution
        
"""
