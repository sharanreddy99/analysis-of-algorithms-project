import json
import os
import sys
from matplotlib import pyplot as plt
from matplotlib.lines import Line2D


def plotDataFromOutputFile():
    yaxisAttributeName = sys.argv[2]
    dataArr = {
        i: {"n": [], "m": [], "respLength": [], "executionTime": []}
        for i in range(1, 5)
    }

    dirList = os.listdir("./output")
    # attributesMap = {
    #     1: {"color": "black", "alpha": 1, "edgecolor": "yellow"},
    #     2: {"color": "yellow", "alpha": 1, "edgecolor": "blue"},
    #     3: {"color": "red", "alpha": 0.6, "edgecolor": "green"},
    #     4: {"color": "blue", "alpha": 0.5, "edgecolor": "yellow"},
    # }
    # for key in dataArr:
    #     for attribute in attributesMap[key]:
    #         dataArr[key][attribute] = attributesMap[key][attribute]

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

    plotDataArr = []

    # No of houses painted
    for key in dataArr:
        plotDataArr.append(
            {
                "data": dataArr[key][yaxisAttributeName],
                "label": dataArr[key]["label"],
            }
        )

    plotHistogramStep(plotDataArr)


def plotHistogram(dataArr):
    for row in dataArr:
        plt.hist(
            row["data"],
            bins=60,
            alpha=row["alpha"],
            label=row["label"],
            color=row["color"],
            edgecolor=row["edgecolor"],
        )

    plt.legend(loc="upper right")
    plt.show()


def plotHistogramStep(dataArr):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(
        [dataArr[i]["data"] for i in range(len(dataArr))],
        bins=60,
        histtype="step",
        linewidth=2,
        alpha=0.7,
        label=[dataArr[i]["label"] for i in range(len(dataArr))],
    )

    handles, labels = ax.get_legend_handles_labels()
    leg_entries = {}
    for h, label in zip(handles, labels):
        leg_entries[label] = Line2D(
            [0],
            [0],
            color=h.get_facecolor()[:-1],
            alpha=h.get_alpha(),
            lw=h.get_linewidth(),
        )

    labels_sorted, lines = zip(*sorted(leg_entries.items()))
    ax.legend(lines, labels_sorted, frameon=False)

    # Remove spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.xlabel("AVAILABILITY OF PAINTER", labelpad=15)
    plt.ylabel("NO OF HOUSES PAINTED", labelpad=15)
    plt.legend(loc="upper right")
    plt.show()
