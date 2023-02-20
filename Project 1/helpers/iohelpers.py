import json
import os
from random import randint
import sys

# import pandas as pd

from .randomlogichelper import task1generator, task2generator, task3generator


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
def generateDummyInput(minV, maxV, task):
    n, m, days = eval("task{0}generator(minV, maxV)".format(task))
    return n, m, days


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
    #         key = (row[0], row[1])
    #         dataMap[key] = dataMap.get(key, [])
    #         dataMap[key].append(row[2])
    #         dataMap[key].append(row[3])

    # rowIdx = pd.MultiIndex.from_tuples(list(dataMap.keys()), names=["n", "m"])
    # colIdx = pd.MultiIndex.from_tuples(colIndices)
    # df = pd.DataFrame(list(dataMap.values()), index=rowIdx, columns=colIdx)

    # with open(filename, "w") as fp:
    #     fp.write(df.style.applymap(lambda x: "color:green;").to_html())


def createFolderIfDoesntExist(path):
    if not os.path.exists(path):
        os.makedirs(path)
