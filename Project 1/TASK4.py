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
        return (
            (self.endDay < other.endDay)
            or ((self.endDay == other.endDay) and (self.startDay < other.startDay))
            or (
                (self.endDay == other.endDay)
                and (self.startDay == other.startDay)
                and (self.index < other.index)
            )
        )


def main(n: int, m: int, days: List[int]) -> List[int]:
    # minHeap contained objects sorted based on shortest duration
    days = [NodeObj(days[i][0], days[i][1], i) for i in range(m)]
    heapq.heapify(days)

    # startDay indicates the current day
    startDay = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    while len(days) > 0:
        node: NodeObj = heapq.heappop(days)
        if startDay < node.startDay:
            startDay = node.startDay

        # if the current house has a endDate less than or equal to current startDate, we paint that house
        if node.endDay <= startDay:
            resultIndicesArr.append(node.index)
            startDay += 1

    return resultIndicesArr


"""

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the starting houses have larger duration than the subsequent houses.
=> n = 5; m = 5; days = [(1,2), (1,3), (1,5), (2, 3), (3, 4)]

Minheap sorted with shortest duration:
    top -> (1, 2) -> (1, 3) -> (2, 3) -> (3, 4) -> (1,5) 
    stack = []

According to current algorithm:
1) House at index 0 is painted on day 1 => 1 lies between (1, 2)
2) House at index 1 is painted on day 2 => 2 lies between (1, 3)
3) House at index 3 is painted on day 3 => 3 lies between (2, 3)
3) House at index 4 is painted on day 4 => 4 lies between (3, 4)
3) House at index 2 is painted on day 5 => 5 lies between (1, 5)
Total number of houses painted = 5 (0, 1, 3, 4, 2)

Optimal Solution:
The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
=> When the houses with higher startDays have a shorter duration than the houses with lower startDays
=> n = 5; m = 4; days = [(1,2), (1,3), (1,4), (1,5)]

Minheap sorted with shortest duration:
    top -> (1,2) -> (1,3) -> (1,4), (1,5)


According to current algorithm:
1) House at index 3 is painted on day 1 => 1 lies between (1, 5)
2) House at index 2 is painted on day 2 => 1 lies between (1, 4)
3) House at index 1 is painted on day 3 => 1 lies between (1, 3)
4) House at index 0 cannot be painted on day 4 or above
Total number of houses painted = 3 (3, 2, 1)

Optimal Solution:
1) House at index 0 is painted on day 1 => 1 lies between (1, 2)
2) House at index 1 is painted on day 2 => 2 lies between (1, 3)
3) House at index 2 is painted on day 3 => 3 lies between (1, 4)
4) House at index 3 is painted on day 4 => 4 lies between (1, 5)
Total number of house painted = 4 (0, 1, 2, 3)

"""


"""
Questions:
    1) (1,3), (2,4), (2,5) => which one is latest (index2 or index3) for startDay = 2
"""
