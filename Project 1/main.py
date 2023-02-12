# Given array is already sorted by startDay and to sorted by endDay to break a tie
import sys
from typing import List

import TASK1
import TASK2
import TASK3
import TASK4


def displayOutput(res) -> None:
    for val in res:
        print(val, end=" ")
    print()


def readInput():
    n, m = map(
        int,
        input(
            "Enter no of days (n) and number of houses (m) separated by spaces"
        ).split(),
    )
    days = []

    # Read the start and end days of the m houses
    for i in range(m):
        days.append(tuple(map(int, input().split())))

    return n, m, days


def readDummyInput():
    # Insert the commented data line from the program file
    n = 5
    m = 4
    days = [(1, 2), (1, 3), (1, 4), (1, 5)]
    return n, m, days


if __name__ == "__main__":
    n, m, days = readDummyInput()
    args = sys.argv
    if len(args) == 2:
        funcCall = "TASK{0}.main(n, m, days)".format(args[1])
        res = eval(funcCall)
        displayOutput(res)
