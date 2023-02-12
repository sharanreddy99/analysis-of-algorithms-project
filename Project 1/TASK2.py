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
            (self.startDay < other.startDay)
            or ((self.startDay == other.startDay) and (self.endDay < other.endDay))
            or (
                (self.startDay == other.startDay)
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

    # stack to store the popped elements from minheap which are not latest to the given house.
    farthestStack: List[NodeObj] = []

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    while not (len(farthestStack) == 0 and len(days) == 0):
        # Removing old latest entries which have their endDay less than current startDay
        while len(farthestStack) > 0 and farthestStack[-1].endDay < startDay:
            farthestStack.pop()

        # Updating the start day to the next closest house
        if len(farthestStack) > 0:
            pass
        elif len(days) > 0:
            if startDay < days[0].startDay:
                startDay = days[0].startDay

        # peeking the top element of minheap and pushing it into the stack if it is a valid latest house
        while len(days) > 0 and days[0].startDay <= startDay:
            farthestStack.append(heapq.heappop(days))

        if len(farthestStack) == 0:
            continue

        # if the current house has a start date greater than or equal to the latest day, we paint that house
        if (
            startDay >= farthestStack[-1].startDay
            and startDay <= farthestStack[-1].endDay
        ):
            node: NodeObj = farthestStack.pop()
            resultIndicesArr.append(node.index)
            startDay += 1

    return resultIndicesArr


"""

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the starting houses have larger duration than the subsequent houses.
=> n = 5; m = 5; days = [(1,5), (1,5), (1,5), (2, 3), (3, 4)]

Minheap sorted with shortest duration:
    top -> (1, 5) -> (1, 5) -> (1, 5) -> (2, 3) -> (3,4) 
    stack = []

According to current algorithm:
1) House at index 2 is painted on day 1 => 1 lies between (1, 5)
2) House at index 3 is painted on day 2 => 2 lies between (2, 3)
3) House at index 4 is painted on day 3 => 3 lies between (3, 4)
3) House at index 1 is painted on day 4 => 4 lies between (1, 5)
3) House at index 0 is painted on day 5 => 5 lies between (1, 5)
Total number of houses painted = 5 (2, 3, 4, 1, 0)

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
