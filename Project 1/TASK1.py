# Algorithm that finds the max houses to be painted based on the first available house
from typing import List


def main(n: int, m: int, days: List[int]) -> List[int]:
    # A pointer to the current house to be painted.
    daysIdx: int = 0

    # An array which stores the indices of houses painted.
    resultIndicesArr: List[int] = []

    for startDay in range(n):
        # we exit the loop as all the intervals have been processed and we are left with no more houses to paint.
        if daysIdx == m:
            break

        # If the current days lies between the start and end days of the house, we paint it.
        if startDay >= days[daysIdx][0] and startDay <= days[daysIdx][1]:
            resultIndicesArr.append(daysIdx)
            daysIdx += 1
            startDay += 1

    return resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(n)
SPACE COMPLEXITY : O(m)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

=> Instance where this algorithm yield an optimal answer?
=> When the startDays are unique, this algorithm gives an optimal solution
=> n = 6; m = 4; days = [(1,2), (2,3), (3,4), (4,5)]

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
=> When the initial houses have longer intervals compared to the subsequent houses, this algorithm gives a non-optimal solution
=> n = 5; m = 4; days = [(1,4), (1,4), (1,4), (2,3)]

=> According to current algorithm:
1) House at index 0 is painted on day 1         => 1 lies between (1, 4)
2) House at index 1 is painted on day 2         => 2 lies between (1, 4)
3) House at index 2 is painted on day 3         => 3 lies between (1, 4)
4) House at index 3 cannot be painted on day 4  => 4 doesn't lie between (2,3)
=> Total number of houses painted = 3 (0, 1, 2)

Optimal Solution:
1) House at index 0 is painted on day 1 => 1 lies between (1, 4)
2) House at index 1 is painted on day 2 => 2 lies between (1, 4)
3) House at index 3 is painted on day 3 => 3 lies between (2, 3)
4) House at index 2 is painted on day 4 => 4 lies between (1, 4)
=> Total number of house painted = 4 (0, 1, 3, 2)
"""
