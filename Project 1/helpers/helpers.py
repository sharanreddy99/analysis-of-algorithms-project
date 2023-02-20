import random
import string
import sys, json

import TASK1, TASK2, TASK3, TASK4, TASK5
from .iohelpers import generateDummyInput, readDummyInput
from .timehelpers import startTimer, returnExecutionTime


# prepareFunctionCall returns the function call string to be executed based on command line arguments
def prepareFunctionCall():
    args = sys.argv
    funcCall = '["Error invalid command line arguments passed!"]'
    if len(args) == 2:
        # reads the first command line argument i.e. a number and calls the respective TASK method
        funcCall = "TASK{0}.main(n, m, days)".format(args[1])
    return funcCall


def compareOptimalTasksWithMultipleInput():
    with open("./output/output.json", "w") as fp:
        args = sys.argv
        for i in range(int(args[5])):
            n, m, days = generateDummyInput(int(args[3]), int(args[4]))
            days.sort()
            fp.write(
                "Input: n ({0}), m: ({1}), days: ${2}\n".format(n, m, json.dumps(days))
            )

            tasks = list(map(int, args[2].split(",")))
            resArr = []
            for task in tasks:
                startTimer()
                res = eval("TASK{0}.main(n, m, days)".format(task))
                resArr.append(res)
                fp.write(
                    "Task - {0}, Length: {1}, Execution Time: {2}, Result: {3}\n".format(
                        task, len(res), returnExecutionTime(), json.dumps(res)
                    )
                )

            for i in range(len(tasks)):
                for j in range(i + 1, len(tasks)):
                    fp.write(
                        "task{0} <= task{1} => {2}\n".format(
                            tasks[i], tasks[j], areResultsEqual(resArr[i], resArr[j])
                        )
                    )

            fp.write("\n\n")


def compareOptimalTasksWithSingleInput():
    with open("./output/output_single.json", "w") as fp:
        args = sys.argv
        n, m, days = readDummyInput()
        if len(args) == 6:
            n, m, days = generateDummyInput(int(args[4]), int(args[5]))
        fp.write(
            "Comparision between task-{0} and task{1}\n_____________________________\n".format(
                int(args[2]), int(args[3])
            )
        )
        fp.write(str(n) + " , " + str(m) + ", " + json.dumps(days) + "\n")
        startTimer()
        res1 = eval("TASK{0}.main(n, m, days)".format(int(args[2])))
        returnExecutionTime()
        fp.write(
            "Task - {0}, Length: {1}, Execution Time: {2}, Result: {3}\n".format(
                int(args[2]), len(res1), returnExecutionTime(), json.dumps(res1)
            )
            + "\n"
        )

        startTimer()
        res2 = eval("TASK{0}.main(n, m, days)".format(int(args[3])))
        returnExecutionTime()
        fp.write(
            "Task - {0}, Length: {1}, Execution Time: {2}, Result: {3}\n".format(
                int(args[3]), len(res2), returnExecutionTime(), json.dumps(res2)
            )
            + "\n"
        )

        fp.write(areResultsEqual(res1, res2))
        fp.write("\n\n")


def areResultsEqual(res1, res2):
    res1.sort()
    res2.sort()
    isEqual = len(res1) <= len(res2)
    if not isEqual:
        for i in range(len(res1)):
            if res1[i] != res2[i]:
                break
        else:
            isEqual = True

    return "True" if isEqual else "False"


def generateRandomInputFile():
    minV = int(sys.argv[2])
    maxV = int(sys.argv[3])
    testCases = int(sys.argv[4])
    task = int(sys.argv[5])
    writeFile = (
        "testcases_" + "".join(random.choices(string.ascii_lowercase, k=8)) + ".txt"
    )

    with open("./input/" + writeFile, "w") as fp:
        for i in range(testCases):
            n, m, days = generateDummyInput(minV, maxV, task)
            fp.write(json.dumps(n) + "\n")
            fp.write(json.dumps(m) + "\n")
            fp.write(json.dumps(days) + "\n")


def runFromTestFile():
    tasks = sys.argv[2].split(",")
    fileName = sys.argv[3]
    fileParts = fileName.split(".")
    fp_opt = open("./output/" + fileParts[0] + "_output." + fileParts[1], "w")
    with open("./input/" + fileName, "r") as fp:
        n = 0
        m = 0
        days = []
        idx = 0
        while True:
            chunk = fp.readline().rstrip("\n ")
            if chunk == "":
                break
            n = int(chunk)

            chunk = fp.readline().rstrip("\n ")
            if chunk == "":
                break
            m = int(chunk)

            chunk = fp.readline().rstrip("\n ")
            if chunk == "":
                break

            days = json.loads(chunk)
            days.sort()
            # task4ResLen = 0
            # task5ResLen = 0
            for task in tasks:
                startTimer()
                res = eval("TASK{0}.main(n, m, days)".format(task))
                respData = {
                    "task": int(task),
                    "n": n,
                    "m": m,
                    "respLength": len(res),
                    "executionTime": returnExecutionTime(),
                }

                # if task == "4":
                #     task4ResLen = len(res)
                # elif task == "5":
                #     task5ResLen = len(res)

                fp_opt.write(json.dumps(respData))
                fp_opt.write("\n")
            # if not (task4ResLen > 0 and task4ResLen == task5ResLen):
            #     print("Found a case")
    fp_opt.close()
