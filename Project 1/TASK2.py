# Algorithm that finds the max houses to be painted based on the latest available house

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

    def __lt__(self, other):
        return (self.startDay < other.startDay) or (
            (self.startDay == other.startDay) and (self.index < other.index)
        )


def main(n: int, m: int, days: List[int]) -> List[int]:
    # latestStartTimeHeap consists of intervals that end the earliest
    latestStartTimeHeap = []
    heapq.heapify(latestStartTimeHeap)

    # startDay indicates the current day
    startDay = 0
    daysIdx = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    for startDay in range(1, n + 1):
        while daysIdx < m and days[daysIdx][0] <= startDay:
            if days[daysIdx][1] >= startDay:
                heapq.heappush(
                    latestStartTimeHeap,
                    NodeObj(-1 * days[daysIdx][0], days[daysIdx][1], -1 * daysIdx),
                )
            daysIdx += 1

        while len(latestStartTimeHeap) > 0:
            node: NodeObj = heapq.heappop(latestStartTimeHeap)
            node.startDay *= -1
            node.index *= -1
            if startDay >= node.startDay and startDay <= node.endDay:
                resultIndicesArr.append(node.index)
                break

    return resultIndicesArr


"""

-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(n + m*logm + m)
SPACE COMPLEXITY : O(n + m) 

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the starting houses have larger duration than the subsequent houses.
=> n = 4; m = 4; days = [(1,5), (1,5), (1,5), (2,3)]

According to current algorithm:
1) House at index 2 is painted on day 1 => 1 lies between (1, 5)
2) House at index 3 is painted on day 2 => 2 lies between (2, 3)
3) House at index 1 is painted on day 3 => 3 lies between (1, 5)
3) House at index 0 is painted on day 4 => 4 lies between (1, 5)
Total number of houses painted = 5 (2, 3, 1, 0)

Optimal Solution:
The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
=> When the initial houses have lower endDays than the subsequent houses
=> n = 5; m = 5; days = [(1,2), (1,3), (1,4), (2, 5), (3, 5)]

According to current algorithm:
1) House at index 2 is painted on day 1 => 1 lies between (1, 4)
2) House at index 3 is painted on day 2 => 1 lies between (2, 5)
3) House at index 4 is painted on day 3 => 1 lies between (3, 5)
4) House at index 0 and index 1 cannot be painted on day 4 or above
Total number of houses painted = 3 (2, 3, 4)

Optimal Solution:
1) House at index 0 is painted on day 1 => 1 lies between (1, 2)
2) House at index 1 is painted on day 2 => 2 lies between (1, 3)
3) House at index 2 is painted on day 3 => 3 lies between (1, 4)
4) House at index 3 is painted on day 4 => 4 lies between (2, 5)
4) House at index 4 is painted on day 5 => 5 lies between (3, 5)
Total number of house painted = 5 (0, 1, 2, 3, 4)

"""
