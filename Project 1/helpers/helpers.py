import sys, json

import TASK1, TASK2, TASK3, TASK4, TASK5
from .iohelpers import generateDummyInput, readDummyInput


# prepareFunctionCall returns the function call string to be executed based on command line arguments
def prepareFunctionCall():
    args = sys.argv
    funcCall = '["Error invalid command line arguments passed!"]'
    if len(args) == 2:
        # reads the first command line argument i.e. a number and calls the respective TASK method
        funcCall = "TASK{0}.main(n, m, days)".format(args[1])
    return funcCall


def compareOptimalTasksWithMultipleInput():
    fp = open("output.json", "w")
    args = sys.argv
    for i in range(100):
        n, m, days = generateDummyInput(int(args[4]), int(args[5]))
        days.sort()
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
        writeIfEqual(fp, res1, res2)
        fp.write("\n\n")
        fp.close()


def compareOptimalTasksWithSingleInput():
    fp = open("output_single.json", "w")
    args = sys.argv
    n, m, days = readDummyInput()
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
    writeIfEqual(fp, res1, res2)
    fp.write("\n\n")
    fp.close()


def writeIfEqual(fp, res1, res2):
    isEqual = False
    if len(res1) == len(res2):
        for i in range(len(res1)):
            if res1[i] != res2[i]:
                break
        else:
            isEqual = True

    if isEqual:
        fp.write("True")
    else:
        fp.write("False")
