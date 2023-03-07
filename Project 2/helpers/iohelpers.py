import json
import os
from random import randint, choices
import string
import sys

# import pandas as pd

from .randomlogichelper import (
    task1generator,
    taskmngenerator,
    taskmkgenerator,
    tasknkgenerator,
)


# DisplayOutput displays the output
def displayOutput(res) -> None:
    for val in res:
        print(val, end=" ")
    print()


# readInput reads input from stdin
def readInput():
    inp = list(map(int, input().split(" ")))

    m, n, h, k = 0, 0, 0, 0
    if len(inp) == 3:
        m, n, h = inp
    else:
        m, n, h, k = inp
    p = []

    # Read the start and end days of the m houses
    for i in range(m):
        inp = list(map(int, input().split(" ")))

        if len(inp) != n:
            print("Invalid input for this row. exiting ")
            exit(0)

        p.append(inp)

    return m, n, h, k, p


# readDummyInput returns a hardcoded input
def readDummyInput():
    # Insert the commented data line from the program file
    m = 3
    n = 4
    h = 3
    k = 3
    p = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

    return m, n, h, k, p


# generateDummyInput generates the dummy data based on user's input requirements
def generateDummyInput(m, n, h, task, maxDiff):
    new_m, new_n, new_h, new_k, new_p = eval(
        "task{0}generator(m, n, h, maxDiff)".format(task)
    )
    return new_m, new_n, new_h, new_k, new_p


def plotPandasTable():
    pass
    # filename = sys.argv[2]
    # foldername = sys.argv[3]
    # tasks = list(map(int, sys.argv[4].split(",")))
    # createFolderIfDoesntExist(foldername)
    # filename = foldername + filename

    # dataArr = {
    #     i: {
    #         "combinedData": [],
    #     }
    #     for i in tasks
    # }

    # dirList = os.listdir("./output")
    # for fileName in dirList:
    #     with open("./output/" + fileName, "r") as fp:
    #         key = "".join(choices(string.ascii_lowercase, k=8))
    #         while True:
    #             chunk = fp.readline().rstrip("\n ")
    #             if chunk == "":
    #                 break
    #             data = json.loads(chunk)
    #             dataArr[data["task"]]["combinedData"].append(
    #                 (
    #                     data["n"],
    #                     data["m"],
    #                     data["respLength"],
    #                     data["executionTime"],
    #                     key,
    #                 )
    #             )

    # for i in tasks:
    #     dataArr[i]["combinedData"].sort(key=lambda x: x[0])

    # dataMap = {}
    # colIndices = []
    # for i in tasks:
    #     colIndices.append(("TASK - " + str(i), "Painted Houses"))
    #     colIndices.append(("TASK - " + str(i), "Execution Time"))

    # for idx in tasks:
    #     for row in dataArr[idx]["combinedData"]:
    #         key = (row[0], row[1], row[4])
    #         dataMap[key] = dataMap.get(key, [])
    #         dataMap[key].append(row[2])
    #         dataMap[key].append(row[3])

    # keys = [key[0:2] for key in dataMap]

    # rowIdx = pd.MultiIndex.from_tuples(list(keys), names=["n", "m"])
    # colIdx = pd.MultiIndex.from_tuples(colIndices)
    # df = pd.DataFrame(list(dataMap.values()), index=rowIdx, columns=colIdx)

    # with open(filename, "w") as fp:
    #     fp.write(df.style.applymap(lambda x: "color:green;").to_html())


def createFolderIfDoesntExist(path):
    if not os.path.exists(path):
        os.makedirs(path)
