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

    def __lt__(self, other):
        temp1 = self.endDay - self.startDay
        temp2 = other.endDay - other.startDay
        return (
            (temp1 < temp2)
            or ((temp1 == temp2) and (self.startDay < other.startDay))
            or (
                (temp1 == temp2)
                and (self.startDay == other.startDay)
                and (self.endDay < other.endDay)
            )
            or (
                (temp1 == temp2)
                and (self.startDay == other.startDay)
                and (self.endDay == other.endDay)
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

        # if the current house has a start date greater than or equal to the current day, we paint that house
        if startDay >= node.startDay and startDay <= node.endDay:
            resultIndicesArr.append(node.index)
            startDay += 1

    return resultIndicesArr


"""

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the difference between endDay and startDay of each house is strictly increasing and the startDays are non decreasing
=> n = 5; m = 4; days = [(1,2), (1,3), (2,5), (3,7)]

Minheap sorted with shortest duration:
	top -> (1,2) -> (1,3) -> (2,5) -> (3,7) 


According to current algorithm:
1) House at index 0 is painted on day 1 => 1 lies between (1, 2)
2) House at index 1 is painted on day 2 => 2 lies between (1, 3)
3) House at index 2 is painted on day 3 => 3 lies between (2, 5)
3) House at index 3 is painted on day 4 => 4 lies between (3, 7)
Total number of houses painted = 4 (0, 1, 2, 3)

Optimal Solution:
The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
=> When the houses with higher startDays have a shorter duration than the houses with lower startDays
=> n = 5; m = 4; days = [(1,3), (2,4), (3,4), (3,6)]

Minheap sorted with shortest duration:
	top -> (3,4) -> (1,3) -> (2,4) -> (3,5)


According to current algorithm:
1) House at index 2 is painted on day 3 => 3 lies between (3, 4)
2) House at index 0 cannot be painted on day 4
3) House at index 1 is painted on day 4 => 4 lies between (2, 4)
4) House at index 3 is painted on day 5 => 5 lies between (3, 5)
Total number of houses painted = 3 (2, 1, 3)

Optimal Solution:
1) House at index 0 is painted on day 1 => 1 lies between (1, 3)
2) House at index 1 is painted on day 2 => 2 lies between (2, 4)
3) House at index 2 is painted on day 3 => 3 lies between (3, 4)
4) House at index 3 is painted on day 4 => 4 lies between (3, 5)
Total number of house painted = 4 (0, 1, 2, 3)

"""
