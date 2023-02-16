import sys
from typing import List
from random import choice


# DisplayOutput displays the output
def displayOutput(res) -> None:
    for val in res:
        print(val, end=" ")
    print()


# readInput reads input from stdin
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


# readDummyInput returns a hardcoded input
def readDummyInput():
    # Insert the commented data line from the program file
    n = 5
    m = 5
    days = [(1, 3), (1, 4), (2, 4), (3, 5), (4, 6)]

    return n, m, days


# generateDummyInput generates the dummy data based on user's input requirements
def generateDummyInput():
    n, m = map(
        int,
        input(
            "Enter number of days (n) and number of houses(m) separated by a space: "
        ).split(),
    )

    start, end = map(
        int,
        input(
            "Enter min start and max end range of the houses separated by space: "
        ).split(),
    )

    days = []
    choiceArr = list(range(start, end + 1))
    while len(days) < m:
        start = choice(choiceArr)
        end = choice(choiceArr)
        if start < end:
            days.append((start, end))

    return n, m, days


# prepareFunctionCall returns the function call string to be executed based on command line arguments
def prepareFunctionCall():
    args = sys.argv
    funcCall = '["Error invalid command line arguments passed!"]'
    if len(args) == 2:
        # reads the first command line argument i.e. a number and calls the respective TASK method
        funcCall = "TASK{0}.main(n, m, days)".format(args[1])

    return funcCall
