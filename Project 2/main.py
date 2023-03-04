# Given array is already sorted by startDay and to sorted by endDay to break a tie
import sys
from helpers import (
    prepareFunctionCall,
    displayOutput,
    readInput,
    compareOptimalTasksWithMultipleInput,
    compareOptimalTasksWithSingleInput,
    generateRandomInputFile,
    runFromTestFile,
    plotDataFromOutputFile,
    plotPandasTable,
)

import TASK1, TASK2, TASK3, TASK4, TASK5A, TASK5B, TASK6, TASK7A, TASK7B


if __name__ == "__main__":
    if sys.argv[1] == "multipleinput":
        compareOptimalTasksWithMultipleInput()
    elif sys.argv[1] == "singleinput":
        compareOptimalTasksWithSingleInput()
    elif sys.argv[1] == "generatetestcases":
        generateRandomInputFile()
    elif sys.argv[1] == "runfromtestfile":
        runFromTestFile()
    elif sys.argv[1] == "plotoutput":
        plotDataFromOutputFile()
    elif sys.argv[1] == "rungentable":
        plotPandasTable()
    else:
        m, n, h, k, p = readInput()
        funcCall = prepareFunctionCall()
        res = []
        if m * n > 0:
            res = eval(funcCall)
        displayOutput(res)
