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
    n = 10000000
    m = 4
    days = [[1, 100], [54023, 56024], [75201, 82063], [99089, 99991]]
    days.sort()

    return n, m, days


# generateDummyInput generates the dummy data based on user's input requirements
def generateDummyInput(minV, maxV):
    n = randint(minV, maxV)
    m = randint(minV, n + 1)
    start = -1
    end = -2
    days = []
    while len(days) < m:
        start = randint(minV, maxV)
        end = randint(minV, maxV)
        if start < end:
            days.append((start, end))

    return n, m, days
