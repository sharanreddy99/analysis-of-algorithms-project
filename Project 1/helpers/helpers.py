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
    with open("output.json", "w") as fp:
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
    with open("output_single.json", "w") as fp:
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
        res1 = eval("TASK{0}.main(n, m, days)".format(int(args[2])))
        res2 = eval("TASK{0}.main(n, m, days)".format(int(args[3])))
        fp.write(json.dumps(res1) + "\n")
        fp.write(json.dumps(res2) + "\n")
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
