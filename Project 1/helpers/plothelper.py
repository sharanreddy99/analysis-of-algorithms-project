import json
import os
import sys

# from matplotlib import pyplot as plt

from helpers.iohelpers import createFolderIfDoesntExist


def plotDataFromOutputFile():
    xaxisAttributeName = sys.argv[2]
    yaxisAttributeName = sys.argv[3]
    xLabel = sys.argv[4]
    yLabel = sys.argv[5]
    filename = sys.argv[6]
    foldername = sys.argv[7]
    tasks = list(map(int, sys.argv[8].split(",")))
    createFolderIfDoesntExist(foldername)
    filename = foldername + filename

    combinedDataKey = "combinedData"
    dataArr = {
        i: {
            "n": [],
            "m": [],
            combinedDataKey: [],
            "respLength": [],
            "executionTime": [],
        }
        for i in tasks
    }

    dirList = os.listdir("./output")
    attributesMap = {
        1: {"borderStyle": "m--"},
        2: {"borderStyle": "r-."},
        3: {"borderStyle": "k-o"},
        4: {"borderStyle": "c-*"},
        5: {"borderStyle": "b->"},
    }
    for key in dataArr:
        for attribute in attributesMap[key]:
            dataArr[key][attribute] = attributesMap[key][attribute]

    for fileName in dirList:
        with open("./output/" + fileName, "r") as fp:
            while True:
                chunk = fp.readline().rstrip("\n ")
                if chunk == "":
                    break
                data = json.loads(chunk)
                for key in data:
                    if key == "task":
                        continue

                    dataArr[data["task"]][key].append(data[key])
                    dataArr[data["task"]]["label"] = "TASK - {0}".format(data["task"])

    for i in tasks:
        dataArr[i][combinedDataKey] = list(
            zip(dataArr[i][xaxisAttributeName], dataArr[i][yaxisAttributeName])
        )
        dataArr[i][combinedDataKey].sort(key=lambda x: x[0])

    plotDataArr = []

    for key in dataArr:
        plotDataArr.append(
            {
                "xData": [row[0] for row in dataArr[key][combinedDataKey]],
                "yData": [row[1] for row in dataArr[key][combinedDataKey]],
                "label": dataArr[key]["label"],
                "borderStyle": dataArr[key]["borderStyle"],
            }
        )

    plotLineGraph(plotDataArr, xLabel, yLabel, filename)


def plotLineGraph(dataArr, xLabel, yLabel, filename):
    pass
    # for row in dataArr:
    #     plt.plot(row["xData"], row["yData"], row["borderStyle"], label=row["label"])

    # plt.xlabel(xLabel, labelpad=5)
    # plt.ylabel(yLabel, labelpad=5)
    # plt.legend(loc="upper left")
    # plt.savefig(filename)
