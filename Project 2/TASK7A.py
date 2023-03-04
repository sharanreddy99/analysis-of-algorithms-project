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
        # We create a three dimensional array with m,n,k as each dimension respectively.
        self.dp = [
            [[-1 for x in range(self.k + 1)] for j in range(self.n + 1)]
            for i in range(self.m + 1)
        ]

        # We initialize all the zeroth index elements on y axis as we chose 1 based indexing to simplify the edge case handling.
        for i in range(self.m + 1):
            for k in range(self.k + 1):
                self.dp[i][0][k] = 0

        # We initialize all the zeroth index elements on x axis as we chose 1 based indexing to simplify the edge case handling.
        for i in range(self.n + 1):
            for k in range(self.k + 1):
                self.dp[0][i][k] = 0

    def compute(self, i, j, k):
        global maxSquareLen, resultIndicesArr

        if k < 0:
            return -1

        # If the maximal square plot at i,j with k exempted plots is already computed, we return the result.
        if self.dp[i][j][k] != -1:
            return self.dp[i][j][k]

        # If the current square has valid number of trees, we find the smallest maximal square plot alongside the boundary of current plot and store it.
        if self.p[i - 1][j - 1] >= self.h:
            self.dp[i][j][k] = 1 + min(self.compute(i, j - 1, k),
                                       self.compute(i - 1, j - 1, k), self.compute(i - 1, j, k))

        # If the current square does not have valid number of trees, we exempt it and find the smallest maximal square plot alongside the boundary of current plot and store it.
        else:
            self.dp[i][j][k] = 1 + min(self.compute(i, j - 1, k - 1), self.compute(
                i - 1, j - 1, k - 1), self.compute(i - 1, j, k - 1))

        # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement without crossing the exempted limit and store it if required.
        if self.dp[i][j][k] > self.maxSquareLen:
            self.resultIndicesArr[0] = i - self.dp[i][j][k] + 1
            self.resultIndicesArr[1] = j - self.dp[i][j][k] + 1
            self.resultIndicesArr[2] = i
            self.resultIndicesArr[3] = j
            self.maxSquareLen = self.dp[i][j][k]

        return self.dp[i][j][k]

    def main(self):
        self.compute(self.m, self.n, self.k)
        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n*k)
SPACE COMPLEXITY : O(m*n*k)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
