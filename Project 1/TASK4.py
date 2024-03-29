# Algorithm that finds the max houses to be painted based on the earliest endDay of each house

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
    # Incase of a tie, it doesn't matter if we pick one with shorter startDay over the other and vice versa as one of them
    # will be left if they fall behind or will be picked if they have sufficiently larger endDay in the future.
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
    # earliestEndDayHeap consists of intervals that end the earliest
    earliestEndDayHeap: List[NodeObj] = []
    heapq.heapify(earliestEndDayHeap)

    daysIdx: int = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    for startDay in range(1, n + 1):
        # We store all the houses that atmost begin at currentDay
        while daysIdx < m and days[daysIdx][0] <= startDay:
            if days[daysIdx][1] >= startDay:
                heapq.heappush(
                    earliestEndDayHeap,
                    NodeObj(days[daysIdx][0], days[daysIdx][1], daysIdx),
                )
            daysIdx += 1

        # We then find the earliest endDay house which includes the current day and paint it.
        while len(earliestEndDayHeap) > 0:
            node: NodeObj = heapq.heappop(earliestEndDayHeap)
            if startDay >= node.startDay and startDay <= node.endDay:
                resultIndicesArr.append(node.index + 1)
                break

    return resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(n + m*logm)
SPACE COMPLEXITY : O(m) 

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> This algorithm will yield an optimal solution for any combination of test cases.
=> n = 5; m = 4; days = [(1,2), (1,3), (1,4), (2, 3)]

According to current algorithm:
1) House at index 1 is painted on day 1 => 1 lies between (1, 2)
2) House at index 2 is painted on day 2 => 2 lies between (1, 3)
3) House at index 4 is painted on day 3 => 3 lies between (2, 3)
3) House at index 3 is painted on day 4 => 4 lies between (1, 4)
Total number of houses painted = 4 (1, 2, 3, 4)
"""
