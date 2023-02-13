# Given array is already sorted by startDay and to sorted by endDay to break a tie
import sys
from typing import List

import TASK1
import TASK2
import TASK3
import TASK4
import TASK5


def displayOutput(res) -> None:
    for val in res:
        print(val, end=" ")
    print()


def readInput():
    n, m = map(
        int,
        input(
            "Enter no of days (n) and number of houses (m) separated by spaces: "
        ).split(),
    )
    days = []

    # Read the start and end days of the m houses
    for i in range(m):
        days.append(
            tuple(
                map(
                    int,
                    input(
                        "Enter startDay, endDay for interval "
                        + str(i + 1)
                        + " sepeareted by a space: "
                    ).split(),
                )
            )
        )

    return n, m, days


def readDummyInput():
    # Insert the commented data line from the program file
    n = 5
    m = 5
    days = [(1, 3), (1, 4), (2, 4), (3, 5), (4, 6)]

    return n, m, days


if __name__ == "__main__":
    n, m, days = readInput()
    args = sys.argv
    if len(args) == 2:
        # reads the first command line argument i.e. a number and calls the respective TASK method
        funcCall = "TASK{0}.main(n, m, days)".format(args[1])
        res = eval(funcCall)
        displayOutput(res)
