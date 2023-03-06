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
        self.dp = [
            [[-1 for x in range(self.n + 1)] for y in range(self.m + 1)]
            for k in range(self.k + 1)
        ]

        # for k in range(self.k + 1):
        #     for j in range(self.n + 1):
        #         self.dp[k][0][j] = 0

        # for k in range(self.k + 1):
        #     for i in range(self.m + 1):
        #         self.dp[k][i][0] = 0

        self.invalidCountArr = [
            [0 for i in range(self.n + 1)] for j in range(self.m + 1)
        ]

        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.invalidCountArr[i][j] = (
                    self.invalidCountArr[i][j - 1]
                    + self.invalidCountArr[i - 1][j]
                    - self.invalidCountArr[i - 1][j - 1]
                    + (1 if self.p[i - 1][j - 1] < self.h else 0)
                )

    def getTopLeft(self, rowEnd, colEnd, dist):
        return rowEnd - dist + 1, colEnd - dist + 1

    def getInvalidCount(self, rowStart, colStart, rowEnd, colEnd):
        invalidCount = self.invalidCountArr[rowEnd][colEnd]
        invalidCount -= self.invalidCountArr[rowStart - 1][colEnd]
        invalidCount -= self.invalidCountArr[rowEnd][colStart - 1]
        invalidCount += self.invalidCountArr[rowStart - 1][colStart - 1]
        return invalidCount

    def computeValidSquare(self, rowEnd, colEnd, dist, k):
        rowStart, colStart = self.getTopLeft(rowEnd, colEnd, dist)
        if rowStart > 0 and colStart > 0:
            invalidCount = self.getInvalidCount(rowStart, colStart, rowEnd, colEnd)
            if invalidCount <= k:
                self.dp[k][rowEnd][colEnd] = max(self.dp[k][rowEnd][colEnd], dist)
                totRows = rowEnd - rowStart + 1
                totCols = colEnd - colStart + 1

                if totRows == totCols and totRows > self.maxSquareLen:
                    self.resultIndicesArr[0] = rowStart
                    self.resultIndicesArr[1] = colStart
                    self.resultIndicesArr[2] = rowEnd
                    self.resultIndicesArr[3] = colEnd
                    self.maxSquareLen = totRows

    def compute(self, rowEnd, colEnd, k):
        if rowEnd == 0 or colEnd == 0:
            self.dp[k][rowEnd][colEnd] = 0
            return 0

        if self.dp[k][rowEnd][colEnd] != -1:
            return self.dp[k][rowEnd][colEnd]

        dist1 = self.compute(rowEnd - 1, colEnd - 1, k)
        self.computeValidSquare(rowEnd, colEnd, dist1 + 1, k)

        dist2 = self.compute(rowEnd - 1, colEnd, k)
        self.computeValidSquare(rowEnd, colEnd, dist2 + 1, k)

        dist3 = self.compute(rowEnd, colEnd - 1, k)
        self.computeValidSquare(rowEnd, colEnd, dist3 + 1, k)

        if k - 1 >= 0:
            dist4 = self.compute(rowEnd - 1, colEnd - 1, k - 1)
            dist5 = self.compute(rowEnd, colEnd, k - 1)
            dist6 = self.compute(rowEnd - 1, colEnd, k - 1)
            dist7 = self.compute(rowEnd, colEnd - 1, k - 1)

            self.computeValidSquare(rowEnd, colEnd, dist4 + 1, k)
            self.computeValidSquare(rowEnd, colEnd, dist5 + 1, k)
            self.computeValidSquare(rowEnd, colEnd, dist6 + 1, k)
            self.computeValidSquare(rowEnd, colEnd, dist7 + 1, k)

        return self.dp[k][rowEnd][colEnd]

    def main(self):
        self.compute(self.m, self.n, self.k)
        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(k*m*n)
SPACE COMPLEXITY : O(k*m*n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
