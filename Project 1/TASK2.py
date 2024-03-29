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

    # Although we are sorting for the smallest startDay and smallest index,
    # we will be passing negative startDay and indices so that the values are sorted in descending order.
    # We will be converting them to positives again once we pop them
    def __lt__(self, other):
        return (
            (self.startDay < other.startDay)
            or ((self.startDay == other.startDay) and (self.endDay < other.endDay))
            or (
                (self.startDay == other.startDay)
                and (self.endDay == other.endDay)
                and (self.index < other.index)
            )
        )


def main(n: int, m: int, days: List[int]) -> List[int]:
    # latestStartTimeHeap consists of intervals that begin the latest until currentDay
    latestStartTimeHeap: List[NodeObj] = []
    heapq.heapify(latestStartTimeHeap)

    daysIdx: int = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    for startDay in range(1, n + 1):
        # We store all the houses that atmost begin at currentDay
        while daysIdx < m and days[daysIdx][0] <= startDay:
            if days[daysIdx][1] >= startDay:
                heapq.heappush(
                    latestStartTimeHeap,
                    NodeObj(-1 * days[daysIdx][0], days[daysIdx][1], -1 * daysIdx),
                )
            daysIdx += 1

        # We then find the latest available house which includes the current day and paint it.
        while len(latestStartTimeHeap) > 0:
            node: NodeObj = heapq.heappop(latestStartTimeHeap)
            node.startDay *= -1
            node.index *= -1
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
=> When the initial houses have longer intervals compared to the subsequent intervals
=> n = 5; m = 4; days = [(1,5), (1,5), (1,5), (2,3)]

According to current algorithm:
1) House at index 3 is painted on day 1 => 1 lies between (1, 5)
2) House at index 4 is painted on day 2 => 2 lies between (2, 3)
3) House at index 2 is painted on day 3 => 3 lies between (1, 5)
3) House at index 1 is painted on day 4 => 4 lies between (1, 5)
Total number of houses painted = 4 (3, 4, 2, 1)

Optimal Solution:
The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
=> When the initial houses have shorter endDays compared to the subsequent intervals.
=> n = 6; m = 5; days = [(1,4), (1,4), (2,5), (3,5), (4, 5)]

According to current algorithm:
1) House at index 2 is painted on day 1 => 1 lies between (1, 4)
2) House at index 3 is painted on day 2 => 2 lies between (2, 5)
3) House at index 4 is painted on day 3 => 3 lies between (3, 5)
3) House at index 5 is painted on day 4 => 4 lies between (4, 5)
4) House at index 1 cannot be painted on day 5 or above
Total number of houses painted = 4 (2, 3, 4, 5)

Optimal Solution:
1) House at index 1 is painted on day 1 => 1 lies between (1, 4)
2) House at index 2 is painted on day 2 => 2 lies between (1, 4)
3) House at index 3 is painted on day 3 => 3 lies between (2, 5)
4) House at index 4 is painted on day 4 => 4 lies between (3, 5)
4) House at index 5 is painted on day 5 => 5 lies between (4, 5)
Total number of house painted = 5 (1, 2, 3, 4, 5)

"""
