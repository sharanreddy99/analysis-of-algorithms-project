import random
import string
import sys
import json

import TASK1
import TASK2
import TASK3
import TASK4
import TASK5A
import TASK5B
import TASK6
import TASK7A
import TASK7B

from .iohelpers import generateDummyInput, readDummyInput
from .timehelpers import startTimer, returnExecutionTime


# prepareFunctionCall returns the function call string to be executed based on command line arguments
def prepareFunctionCall(task=None):
    funcCall = '["Error invalid command line arguments passed!"]'
    if len(sys.argv) == 2:
        task = sys.argv[1]

    if "6" in task or "7" in task:
        funcCall = "TASK{0}.Main(m, n, h, k, p).main()".format(task.lstrip("run"))
    else:
        funcCall = "TASK{0}.Main(m, n, h, p).main()".format(task.lstrip("run"))

    return funcCall


def compareOptimalTasksWithMultipleInput():
    with open("./output/output.json", "w") as fp:
        args = sys.argv
        for i in range(int(args[6])):
            m, n, h, k, p = generateDummyInput(
                int(args[3]), int(args[4]), int(args[5]), int(args[7]), int(args[8])
            )
            fp.write(
                "Input: m ({0}), n: ({1}), h: ({2}), k: ({3}), p: {4}\n".format(
                    m, n, h, k, json.dumps(p)
                )
            )

            tasks = args[2].split(",")
            resArr = []
            for task in tasks:
                startTimer()
                res = eval(prepareFunctionCall(task))
                resArr.append(res)
                fp.write(
                    "Task - {0}, Execution Time: {1}, Result: {2}\n".format(
                        task, returnExecutionTime(), json.dumps(res)
                    )
                )

            for i in range(len(tasks)):
                for j in range(i + 1, len(tasks)):
                    fp.write(
                        "task{0} == task{1} => {2}\n".format(
                            tasks[i],
                            tasks[j],
                            areResultsEqual(resArr[i], resArr[j], h, k, p),
                        )
                    )
                    if areResultsEqual(resArr[i], resArr[j], h, k, p) == "False":
                        print(
                            "m: ({0}), n: ({1}), h: ({2}), k: ({3}) p:{4}, taska: ({5}), taskb: ({6}), res1: ({7}), res2: ({8})".format(
                                m, n, h, k, p, tasks[i], tasks[j], resArr[i], resArr[j]
                            )
                        )
            fp.write("\n\n")


def compareOptimalTasksWithSingleInput():
    with open("./output/output_single.json", "w") as fp:
        args = sys.argv
        m, n, h, k, p = readDummyInput()
        if len(args) == 8:
            m, n, h, k, p = generateDummyInput(
                int(args[4]), int(args[5]), int(args[6]), int(args[7]), int(args[8])
            )
        fp.write(
            "Comparision between task-{0} and task-{1}\n_____________________________\n".format(
                int(args[2]), int(args[3])
            )
        )
        fp.write(
            str(m)
            + " , "
            + str(n)
            + ", "
            + str(h)
            + ", "
            + str(k)
            + ","
            + json.dumps(p)
            + "\n"
        )
        startTimer()
        res1 = eval(prepareFunctionCall(args[2]))
        returnExecutionTime()
        fp.write(
            "Task - {0}, Execution Time: {1}, Result: {2}\n".format(
                args[2], returnExecutionTime(), json.dumps(res1)
            )
            + "\n"
        )

        startTimer()
        res2 = eval(prepareFunctionCall(args[3]))
        returnExecutionTime()
        fp.write(
            "Task - {0}, Execution Time: {1}, Result: {2}\n".format(
                args[3], returnExecutionTime(), json.dumps(res2)
            )
            + "\n"
        )
        fp.write(areResultsEqual(res1, res2, h, k, p))
        fp.write("\n\n")


def areResultsEqual(res1, res2, h, k, p):
    maxLen1 = (res1[2] - res1[0] + 1) * (res1[3] - res1[1] + 1)
    maxLen2 = (res2[2] - res2[0] + 1) * (res2[3] - res2[1] + 1)
    invalidCount1 = 0
    invalidCount2 = 0

    for i in range(res1[0], res1[2] + 1):
        for j in range(res1[1], res1[3] + 1):
            if p[i - 1][j - 1] < h:
                invalidCount1 += 1

    for i in range(res2[0], res2[2] + 1):
        for j in range(res2[1], res2[3] + 1):
            if p[i - 1][j - 1] < h:
                invalidCount2 += 1

    return (
        "True"
        if (
            maxLen1 == maxLen2
            and (
                (invalidCount1 <= k and invalidCount2 <= k)
                or (res1 == [-1, -1, -1, -1] and res2 == [-1, -1, -1, -1])
            )
        )
        else "False"
    )


def generateRandomInputFile():
    m = int(sys.argv[2])
    n = int(sys.argv[3])
    h = int(sys.argv[4])
    testCases = int(sys.argv[5])
    task = int(sys.argv[6])
    maxDiff = int(sys.argv[7])
    writeFile = (
        "testcases_" + "".join(random.choices(string.ascii_lowercase, k=8)) + ".txt"
    )

    with open("./input/" + writeFile, "w") as fp:
        for i in range(testCases):
            new_m, new_n, new_h, new_k, new_p = generateDummyInput(
                m, n, h, task, maxDiff
            )
            fp.write(json.dumps(new_m) + "\n")
            fp.write(json.dumps(new_n) + "\n")
            fp.write(json.dumps(new_h) + " " + json.dumps(new_k) + "\n")
            fp.write(json.dumps(new_p) + "\n")


def runFromTestFile():
    tasks = sys.argv[2].split(",")
    fileName = sys.argv[3]
    fileParts = fileName.split(".")
    fp_opt = open(
        "./output/{0}_output_{1}.{2}".format(fileParts[0], tasks, fileParts[1]), "w"
    )
    with open("./input/" + fileName, "r") as fp:
        n = 0
        m = 0
        h = 0
        k = 0
        p = []
        while True:
            chunk = fp.readline().rstrip("\n ")
            if chunk == "":
                break
            m = int(chunk)

            chunk = fp.readline().rstrip("\n ")
            if chunk == "":
                break
            n = int(chunk)

            chunk = fp.readline().rstrip("\n ")
            if chunk == "":
                break

            chunkArr = chunk.split(" ")
            h = int(chunkArr[0])

            if len(chunkArr) == 2:
                k = int(chunkArr[1])

            chunk = fp.readline().rstrip("\n ")
            if chunk == "":
                break

            p = json.loads(chunk)
            for task in tasks:
                startTimer()
                res = eval(prepareFunctionCall(task))
                respData = {
                    "task": task,
                    "m": m,
                    "n": n,
                    "h": h,
                    "resp": res,
                    "executionTime": returnExecutionTime(),
                }

                if "6" in task or "7" in task:
                    respData["k"] = k

                fp_opt.write(json.dumps(respData))
                fp_opt.write("\n")
            fp_opt.write("\n")
    fp_opt.close()
