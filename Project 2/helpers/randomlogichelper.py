from random import randint


def task1generator(m, n, h, maxDiff):
    new_m = randint(2, m)
    new_n = randint(2, n)
    new_k = randint(0, max(new_m, new_n))

    p = [[0 for j in range(new_n)] for i in range(new_m)]

    for i in range(new_m):
        for j in range(new_n):
            p[i][j] = randint(h - maxDiff, h + maxDiff)

    return new_m, new_n, h, new_k, p
