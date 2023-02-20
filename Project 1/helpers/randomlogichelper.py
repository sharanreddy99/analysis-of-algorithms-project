import math
from random import randint


def task1generator(minV, maxV):
    n = randint(minV, maxV)
    m = randint(minV, n)
    start = -1
    end = -2
    days = []
    while len(days) < m:
        start = randint(minV, n)
        end = randint(start + 1, maxV)
        if start < end:
            days.append((start, end))

    return n, m, days


def task2generator(minV, maxV):
    n = randint(minV, maxV)
    m = randint(minV, n)
    start = -1
    end = -2
    days = []

    if m // 10 == 0:
        m += 10
        n += 10

    while len(days) < m // 10:
        start = randint(minV, n)
        end = randint(start + 1, maxV)
        if start < end:
            days.append((start, end))

    idx = 0
    while len(days) < (4 * m) // 10:
        start = randint(minV, n)
        difference = days[idx][1] - days[idx][0]
        end = start + difference
        if start < end:
            days.append((start, end))
            idx = (idx + 1) % (m // 10)

    while len(days) < m:
        start = randint(minV, n)
        end = randint(start + 1, maxV)
        if start < end:
            days.append((start, end))

    return n, m, days


def task3generator(minV, maxV):
    n = randint(minV, maxV)
    m = randint(minV, n)
    if m < 5:
        m += 5
        n += 5

    start = -1
    end = -2
    days = []

    while len(days) < m:
        start = randint(minV, math.sqrt(n) // 1)
        end = start
        if start + 1 < n:
            end = randint(start + 1, n)
        if start + 1 < end:
            days.append((start, end))
            counter = end - start + 1
            while len(days) < m and counter > 0:
                newstart = randint(start, end)
                newend = newstart
                if newstart + 1 < end:
                    newend = randint(newstart + 1, end)
                if newstart < newend:
                    days.append((newstart, newend))
                    counter -= 1

    return n, m, days
