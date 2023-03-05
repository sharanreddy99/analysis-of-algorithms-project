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
        # Stores the count of square plots less than h.
        self.dp = [0 for i in range(self.n)]

    def main(self):
        # The first two loops fix the upper left corner for the given square plot.
        for rowStart in range(self.m):
            for colStart in range(self.n):
                # Clear the previous memorized values
                for x in range(self.n):
                    self.dp[x] = 0

                # The next two loops fix the lower right corner for the square plot whose upper left corner is fixed and compute the no of mintree plots
                # in the given square based on the precomputed value from the previous row.
                for rowEnd in range(rowStart, self.m):
                    for colEnd in range(colStart, self.n):
                        self.dp[rowEnd][colEnd] += (
                            1 if self.p[rowEnd][colEnd] >= self.h else 0
                        )

                        totRows = rowEnd - rowStart + 1
                        totCols = colEnd - colStart + 1

                        # We check whether the chosen plot is an optimal square plot satisfying the min tree requirement and store it if required.
                        if (
                            totRows == totCols
                            and self.dp[rowEnd][colEnd] == totRows * totCols
                            and totRows > self.maxSquareLen
                        ):
                            self.resultIndicesArr[0] = rowStart + 1
                            self.resultIndicesArr[1] = colStart + 1
                            self.resultIndicesArr[2] = rowEnd + 1
                            self.resultIndicesArr[3] = colEnd + 1
                            self.maxSquareLen = totRows

        return self.resultIndicesArr


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------
TIME COMPLEXITY  : O(m*n*m*n)
SPACE COMPLEXITY : O(n)

-----------------------------------------------------------------------------------------------------------------------------------------------------------
"""
