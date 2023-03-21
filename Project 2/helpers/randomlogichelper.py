import random


def task1generator(m, n, h, maxDiff):
    new_m = random.randint(2, m)
    new_n = random.randint(2, n)
    new_k = random.randint(0, max(new_m, new_n))

    p = [[0 for j in range(new_n)] for i in range(new_m)]

    for i in range(new_m):
        for j in range(new_n):
            p[i][j] = random.randint(h - maxDiff, h + maxDiff)

    return new_m, new_n, h, new_k, p


def taskmngenerator(m, n, h, maxDiff):
    new_m = m
    new_n = n
    new_k = random.randint(0, new_m * new_n)

    p = [[0 for j in range(new_n)] for i in range(new_m)]
    customRandom = random.Random(12)
    for i in range(new_m):
        for j in range(new_n):
            p[i][j] = customRandom.randint(h - maxDiff, h + maxDiff)

    return new_m, new_n, h, new_k, p


def taskmkgenerator(m, n, h, maxDiff):
    new_m = m
    new_n = random.randint(0, n + 1)
    new_k = 4

    p = [[0 for j in range(new_n)] for i in range(new_m)]

    for i in range(new_m):
        for j in range(new_n):
            p[i][j] = random.randint(h - maxDiff, h + maxDiff)

    return new_m, new_n, h, new_k, p


def tasknkgenerator(m, n, h, maxDiff):
    new_m = random.randint(0, m + 1)
    new_n = n
    new_k = 4

    p = [[0 for j in range(new_n)] for i in range(new_m)]

    for i in range(new_m):
        for j in range(new_n):
            p[i][j] = random.randint(h - maxDiff, h + maxDiff)

    return new_m, new_n, h, new_k, p
