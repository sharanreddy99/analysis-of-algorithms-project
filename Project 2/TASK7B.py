class Main:
    def __init__(self, m, n, h, k, p):
        # No of rows
        self.m = m

        # No of cols
        self.n = n

        # Min number of trees
        self.h = h

        # Trees planted on each plot
        self.p = p

        # No of exempted square plots
        self.k = k

        # Array which stores the top left and bottom right indices sequentially
        self.resultIndicesArr = [-1, -1, -1, -1]

        # Size of the maximal square plot
        self.maxSquareLen = 0

        self.initDPArray()

    def initDPArray(self):
        # We create a three dimensional array with 2,n,k as each dimension respectively.
        # We only consider two dimensions in x axis as we require only the previous row to compute the optimal solution.
        self.dp = [
            [[0 for x in range(self.k + 1)] for j in range(self.n + 1)]
            for i in range(2)
        ]

    def main(self):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                for x in range(self.k + 1):
                    # If the current square has valid number of trees, we find the smallest maximal square plot alongside the boundary of current plot and store it.
                    if self.p[i - 1][j - 1] >= self.h:
                        self.dp[i % 2][j][x] = 1 + min(self.dp[(i - 1) % 2][j][x], self.dp[(
                            i - 1) % 2][j - 1][x], self.dp[i % 2][j - 1][x])

                    # If the current square does not have valid number of trees, we exempt it and find the smallest maximal square plot alongside the boundary of current plot and store it.
                    elif x - 1 >= 0:
                        self.dp[i % 2][j][x] = 1 + min(self.dp[(i - 1) % 2][j][x - 1], self.dp[(
                            i - 1) % 2][j - 1][x - 1], self.dp[i % 2][j - 1][x - 1], )

                    # We dont have any optimal square plots that end at current plot which satisfy the requirement. Hence, we clear it.
                    else:
                        self.dp[i % 2][j][x] = 0

                    # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement without crossing the exempted limit and store it if required.
                    if self.dp[i % 2][j][x] > self.maxSquareLen:
                        self.maxSquareLen = self.dp[i % 2][j][x]
                        self.resultIndicesArr[0] = i - self.dp[i % 2][j][x] + 1
                        self.resultIndicesArr[1] = j - self.dp[i % 2][j][x] + 1
                        self.resultIndicesArr[2] = i
                        self.resultIndicesArr[3] = j

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n*k)
SPACE COMPLEXITY : O(n*k)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
