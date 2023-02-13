# Algorithm that finds the max houses to be painted based on the shortest duration of the house
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

    # We sort based on the shortest duration for a given house and in case of a tie, we sort secondarily on endDay and index.
    # Note that if duration and endDays are same, this indicates that startDay is also same. Hence we are not comparing that value.
    def __lt__(self, other):
        temp1 = self.endDay - self.startDay
        temp2 = other.endDay - other.startDay
        return (
            (temp1 < temp2)
            or ((temp1 == temp2) and (self.endDay < other.endDay))
            or (
                (temp1 == temp2)
                and (self.endDay == other.endDay)
                and (self.index < other.index)
            )
        )


def main(n: int, m: int, days: List[int]) -> List[int]:
    # shortestDurationHeap consists of intervals that have the smallest duration
    shortestDurationHeap = []
    heapq.heapify(shortestDurationHeap)

    daysIdx = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    for startDay in range(1, n + 1):
        # We store all the houses that atmost begin at currentDay
        while daysIdx < m and days[daysIdx][0] <= startDay:
            if days[daysIdx][1] >= startDay:
                heapq.heappush(
                    shortestDurationHeap,
                    NodeObj(days[daysIdx][0], days[daysIdx][1], daysIdx),
                )
            daysIdx += 1

        # We then find the shortest duration house which includes the current day and paint it.
        while len(shortestDurationHeap) > 0:
            node: NodeObj = heapq.heappop(shortestDurationHeap)
            if startDay >= node.startDay and startDay <= node.endDay:
                resultIndicesArr.append(node.index)
                break

    return resultIndicesArr


"""

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the initial houses have larger duration than the subsequent houses
=> n = 4; m = 4; days = [(1,2), (1,4), (2,3), (3,4)]

According to current algorithm:
1) House at index 0 is painted on day 1 => 1 lies between (1, 2)
2) House at index 2 is painted on day 2 => 2 lies between (2, 3)
3) House at index 3 is painted on day 3 => 3 lies between (3, 4)
3) House at index 1 is painted on day 4 => 4 lies between (1, 4)
Total number of houses painted = 4 (0, 2, 3, 1)

Optimal Solution:
The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
=> When the initial houses have sort of larger duration than the subsequent houses but the later houses have sufficient duration to paint
=> n = 5; m = 5; days = [(1,3), (1,4), (2,4), (3,5), (4,6)]

According to current algorithm:
1) House at index 0 is painted on day 1 => 1 lies between (1, 3)
2) House at index 2 is painted on day 2 => 2 lies between (2, 4)
3) House at index 3 is painted on day 3 => 4 lies between (3, 5)
4) House at index 4 is painted on day 4 => 5 lies between (4, 6)
Total number of houses painted = 4 (0, 2, 3, 4)

Optimal Solution:
1) House at index 0 is painted on day 1 => 1 lies between (1, 3)
2) House at index 1 is painted on day 2 => 2 lies between (1, 4)
3) House at index 2 is painted on day 3 => 3 lies between (2, 4)
4) House at index 3 is painted on day 4 => 4 lies between (3, 5)
5) House at index 4 is painted on day 5 => 5 lies between (4, 6)
Total number of house painted = 5 (0, 1, 2, 3, 4)

"""
