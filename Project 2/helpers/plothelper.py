import json
import os
import sys

# from matplotlib import pyplot as plt
# import numpy as np

from helpers.iohelpers import createFolderIfDoesntExist


def plotDataFromOutputFile():
    xaxisAttributeName = sys.argv[2]
    yaxisAttributeName = sys.argv[3]
    xLabel = sys.argv[4]
    yLabel = sys.argv[5]
    filename = sys.argv[6]
    foldername = sys.argv[7] + xaxisAttributeName + "/"
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
        "3": {"borderStyle": "y-o", "color": "#bc5090"},
        "4": {"borderStyle": "m--", "color": "#ffa600"},
        "5A": {"borderStyle": "r-.", "color": "#ff6361"},
        "5B": {"borderStyle": "y-o", "color": "#bc5090"},
        "6": {"borderStyle": "m--", "color": "#ffa600"},
        "7A": {"borderStyle": "r-.", "color": "#ff6361"},
        "7B": {"borderStyle": "y-o", "color": "#bc5090"},
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
                    chunk = fp.readline().rstrip("\n ")
                    if chunk == "":
                        break
                data = json.loads(chunk)
                for key in data:
                    if key == "task":
                        continue

                    if dataArr.get(data["task"]) == None:
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

    # plotBarGraph(plotDataArr, xLabel, yLabel, filename)
    plotLineGraph(plotDataArr, xLabel, yLabel, filename)


def plotLineGraph(dataArr, xLabel, yLabel, fileName):
    pass
    # _, ax = plt.subplots(constrained_layout=True)
    # for row in dataArr:
    #     ax.plot(row["xData"], row["yData"], row["borderStyle"], label=row["label"])

    # ax.set_xlabel(xLabel, labelpad=10)
    # ax.set_ylabel(yLabel, labelpad=10)
    # ax.set_title(
    #     "{0} vs {1} when the other metrics are constant".format(xLabel, yLabel)
    # )
    # ax.legend(loc="upper left")
    # fileParts = fileName.split(".")
    # fileName = ".".join([fileParts[0], fileParts[1] + "_line", fileParts[2]])
    # plt.savefig(fileName)


def plotBarGraph(dataArr, xLabel, yLabel, fileName):
    pass
    # xAxisData = dataArr[0]["xData"]
    # yAxisData = {dataArr[i]["label"]: dataArr[i]["yData"] for i in range(len(dataArr))}
    # colors = {dataArr[i]["label"]: dataArr[i]["color"] for i in range(len(dataArr))}

    # x = np.arange(len(xAxisData))
    # width = 0.25
    # multiplier = 0

    # _, ax = plt.subplots(constrained_layout=True)

    # for label, valArr in yAxisData.items():
    #     offset = width * multiplier
    #     rects = ax.bar(x + offset, valArr, width, label=label, color=colors[label])
    #     multiplier += 1

    # # Add some text for labels, title and custom x-axis tick labels, etc.
    # ax.set_xlabel(xLabel)
    # ax.set_ylabel(yLabel)
    # ax.set_title(
    #     "{0} vs {1} when the other metrics are constant".format(xLabel, yLabel)
    # )
    # ax.set_xticks(x + width, xAxisData)
    # ax.legend(loc="upper left", ncols=1)

    # fileParts = fileName.split(".")
    # fileName = ".".join([fileParts[0], fileParts[1] + "_bar", fileParts[2]])
    # plt.savefig(fileName)
