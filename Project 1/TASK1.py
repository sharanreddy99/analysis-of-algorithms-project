# Algorithm that finds the max houses to be painted based on the earliest available house
from typing import List


def main(n: int, m: int, days: List[int]) -> List[int]:
    # A pointer to the current house to be painted.
    daysIdx: int = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    for startTime in range(1, n + 1):
        if daysIdx == m:
            break

        # If the current days lies between the start and end days of the house, we paint it.
        if startTime >= days[daysIdx][0] and startTime <= days[daysIdx][1]:
            resultIndicesArr.append(daysIdx)
            daysIdx += 1

    return resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the start dates of each house are arranged in strictly increasing order
=> n = 5; m = 4; days = [(1,2), (2,3), (3,4), (4,5)]

=> According to current algorithm:
1) House at index 0 is painted on day 1 => 1 lies between (1, 2)
2) House at index 1 is painted on day 2 => 2 lies between (2, 3)
3) House at index 2 is painted on day 3 => 3 lies between (3, 4)
4) House at index 3 is painted on day 4 => 4 lies between (4, 5)
Total number of houses painted = 4 (0, 1, 2, 3)

Optimal Solution:
=> The above solution is the optimal one as it paints all the houses available

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm doesn't yield an optimal answer?
=> When the initial houses have a large deadline with them and the next houses have a short deadline
=> n = 5; m = 4; days = [(1,3), (1,4), (1,5), (2,3)]

=> According to current algorithm:
1) House at index 0 is painted on day 1 => 1 lies between (1, 3)
2) House at index 1 is painted on day 2 => 2 lies between (1, 4)
3) House at index 2 is painted on day 3 => 3 lies between (1, 5)
4) House at index 3 cannot be painted   => 4 doesn't lie between (2,3)
=> Total number of houses painted = 3 (0, 1, 2)

Optimal Solution:
1) No house is painted on day 1
2) House at index 3 is painted on day 2 => 2 lies between (2, 3)
3) House at index 0 is painted on day 3 => 3 lies between (1, 3)
4) House at index 1 is painted on day 4 => 4 lies between (1, 4)
5) House at index 2 is painted on day 5 => 5 lies between (1, 5)
=> Total number of house painted = 4 (3, 0, 1, 2)
"""
