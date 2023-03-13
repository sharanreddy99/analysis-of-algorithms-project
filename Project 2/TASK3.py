# Given a matrix p of m ×n integers (non-negative) representing the minimum number of trees that must be planted on each plot and an integer h (positive), find the bounding indices of a square area where each plot enclosed requires a minimum of h trees to be planted
# Design a Θ(m * n) time Dynamic Programming algorithm for solving Problem1
class Main:
    def __init__(self, m, n, h, p):
        # No of rows
        self.m = m

        # No of cols
        self.n = n

        # Min number of trees
        self.h = h

        # Trees planted on each plot
        self.p = p

        # Array which stores the top left and bottom right indices sequentially
        self.resultIndicesArr = [-1, -1, -1, -1]

        # Size of the maximal square plot
        self.maxSquareLen = 0

        self.initDPArray()

    def initDPArray(self):
        # DP[i,j] indicates the size of the largest square plot whose bottomRight corner is i,j
        self.dp = [[0 for j in range(self.n + 1)] for i in range(2)]

    def main(self):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                # If the current square has valid number of trees, we find the smallest maximal square plot alongside the boundary of current plot and store it.
                if self.p[i - 1][j - 1] >= self.h:
                    self.dp[i % 2][j] = (
                        min(
                            self.dp[(i - 1) % 2][j],
                            self.dp[(i - 1) % 2][j - 1],
                            self.dp[i % 2][j - 1],
                        )
                        + 1
                    )

                # We don't have any maximal square plots ending at current plot
                else:
                    self.dp[i % 2][j] = 0

                # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement and store it if bigger than the previous maximal result.
                if self.dp[i % 2][j] > self.maxSquareLen:
                    self.resultIndicesArr[0] = i - self.dp[i % 2][j] + 1
                    self.resultIndicesArr[1] = j - self.dp[i % 2][j] + 1
                    self.resultIndicesArr[2] = i
                    self.resultIndicesArr[3] = j
                    self.maxSquareLen = self.dp[i % 2][j]

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m * n)
SPACE COMPLEXITY : O(n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
