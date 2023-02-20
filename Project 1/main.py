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

import TASK1
import TASK2
import TASK3
import TASK4
import TASK5


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
        n, m, days = readInput()
        days.sort()
        funcCall = prepareFunctionCall()
        res = []
        if len(days) > 0:
            res = eval(funcCall)
        displayOutput(res)
