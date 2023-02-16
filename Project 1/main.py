# Given array is already sorted by startDay and to sorted by endDay to break a tie
from helpers import generateDummyInput, prepareFunctionCall, displayOutput, readInput

import TASK1
import TASK2
import TASK3
import TASK4
import TASK5


if __name__ == "__main__":
    n, m, days = readInput()
    funcCall = prepareFunctionCall()
    res = []
    if len(days) > 0:
        res = eval(funcCall)
    displayOutput(res)
