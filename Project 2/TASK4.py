# Algorithm that finds the max houses to be painted based on the first available house
from typing import List


def main(m: int, n: int, h: int, p: List[int]) -> List[int]:
    # An array which stores the top left and bottom right indices of the maximal square plot.
    resultIndicesArr: List[int] = [-1, -1, -1, -1]

    # An integer which stores the no of rows in the maximal square plot.
    maxSquareLen = 0

    # an array which stores the optimal square plot length including current position.
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            topLeftRow = i + 1
            topLeftCol = j + 1

            for k in range(min(m - i + 1, n - j + 1)):
                bottomLeftRow = i + k - 1
                bottomRightRow = j + k - 1

            if p[i - 1][j - 1] >= h:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

                if dp[i][j] > maxSquareLen:
                    maxSquareLen = dp[i][j]
                    resultIndicesArr = [i - dp[i][j] + 1, j - dp[i][j] + 1, i, j]

    return resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n)
SPACE COMPLEXITY : O(m*n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
