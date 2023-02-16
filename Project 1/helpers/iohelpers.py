from random import choice, randint


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
    n = 83
    m = 3
    days = [[7, 80], [10, 63], [64, 70]]
    days.sort()

    return n, m, days


# generateDummyInput generates the dummy data based on user's input requirements
def generateDummyInput(minV, maxV):
    n = randint(minV, maxV)
    m = randint(minV, maxV)
    start = -1
    end = -2
    while start >= end:
        start = randint(minV, maxV)
        end = randint(minV, maxV)

    days = []
    while len(days) < m:
        start = randint(minV, n)
        end = randint(minV, n)
        if start < end:
            days.append((start, end))

    return n, m, days
