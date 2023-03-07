import json
import os
import sys

from matplotlib import pyplot as plt
import numpy as np

from helpers.iohelpers import createFolderIfDoesntExist


def plotDataFromOutputFile():
    xaxisAttributeName = sys.argv[2]
    yaxisAttributeName = sys.argv[3]
    xLabel = sys.argv[4]
    yLabel = sys.argv[5]
    filename = sys.argv[6]
    foldername = sys.argv[7]
    tasks = sys.argv[8].split(",")
    createFolderIfDoesntExist(foldername)
    filename = foldername + filename

    combinedDataKey = "combinedData"
    dataArr = {
        i: {
            "m": [],
            "n": [],
            "h": [],
            "k": [],
            combinedDataKey: [],
            "resp": [],
            "executionTime": [],
        }
        for i in tasks
    }

    dirList = os.listdir("./output")
    attributesMap = {
        "1": {"borderStyle": "m--", "color": "#ffa600"},
        "2": {"borderStyle": "r-.", "color": "#ff6361"},
        "3": {"borderStyle": "k-o", "color": "#bc5090"},
        "4": {"borderStyle": "m--", "color": "#ffa600"},
        "5A": {"borderStyle": "r-.", "color": "#ff6361"},
        "5B": {"borderStyle": "k-o", "color": "#bc5090"},
        "6": {"borderStyle": "m--", "color": "#ffa600"},
        "7A": {"borderStyle": "r-.", "color": "#ff6361"},
        "7B": {"borderStyle": "k-o", "color": "#bc5090"},
    }

    for key in dataArr:
        for attribute in attributesMap[key]:
            dataArr[key][attribute] = attributesMap[key][attribute]

    for fileName in dirList:
        if "".join(tasks) not in fileName:
            continue

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
                "color": dataArr[key]["color"],
            }
        )

    plotLineGraph(plotDataArr, xLabel, yLabel, filename)


def plotLineGraph(dataArr, xLabel, yLabel, filename):
    for row in dataArr:
        plt.plot(row["xData"], row["yData"], row["borderStyle"], label=row["label"])

    plt.xlabel(xLabel, labelpad=10)
    plt.ylabel(yLabel, labelpad=10)
    plt.legend(loc="upper left")
    plt.savefig(filename)


def plotBarGraph(dataArr, xLabel, yLabel, fileName):
    pass
    # xAxisData = dataArr[0]["xData"]
    # yAxisData = {
    #     "TASK - {0}".format(i + 1): dataArr[i]["yData"] for i in range(len(dataArr))
    # }

    # colors = {
    #     "TASK - {0}".format(i + 1): dataArr[i]["color"] for i in range(len(dataArr))
    # }

    # x = np.arange(len(xAxisData))
    # width = 0.15
    # multiplier = 0

    # _, ax = plt.subplots(constrained_layout=True)

    # for label, valArr in yAxisData.items():
    #     offset = width * multiplier
    #     rects = ax.bar(x + offset, valArr, width, label=label, color=colors[label])
    #     multiplier += 1

    # # Add some text for labels, title and custom x-axis tick labels, etc.
    # ax.set_xlabel(xLabel)
    # ax.set_ylabel(yLabel)
    # ax.set_title("{0} vs {1} when m = {2}".format(xLabel, yLabel, dataArr[0]["m"]))
    # ax.set_xticks(x + width, xAxisData)
    # ax.legend(loc="upper left", ncols=1)

    # plt.savefig(fileName)
