import json
from os import abort
from random import random, choices
import string
from flask import Flask,request, send_from_directory

import TASK1,TASK2, TASK3, TASK4, TASK5
from helpers.timehelpers import startTimer, returnExecutionTime
from helpers.iohelpers import generateDummyInput

app = Flask(__name__)


@app.route("/tasks/execute", methods=["POST"])
def executeTask():
    requestBody = request.json
    n = requestBody["n"]
    m = requestBody["m"]
    days = requestBody["days"]
    tasks = requestBody["tasks"]

    resMap = {}
    for task in tasks:
        resMap[task] = eval("TASK{0}.main(n, m, days)".format(task))

    return "<p>{0}</p>".format(json.dumps(resMap))

@app.route("/tasks/file/generate", methods=["GET"])
def generateTask():
    try:
        requestArgs = request.args.to_dict()
        minV = int(requestArgs["minval"])
        maxV = int(requestArgs["maxval"])
        testCases = int(requestArgs["testcases"])
        task = int(requestArgs["task"])

        writeFile = (
            "testcases_" + "".join(choices(string.ascii_lowercase, k=8)) + ".txt"
        )

        with open("./input/" + writeFile, "w") as fp:
            for i in range(testCases):
                n, m, days = generateDummyInput(minV, maxV, task)
                fp.write(json.dumps(n) + "\n")
                fp.write(json.dumps(m) + "\n")
                fp.write(json.dumps(days) + "\n")

        return send_from_directory("./input/", writeFile, as_attachment=True)
    except Exception as e:
        print(e)

@app.route("/tasks/file/execute", methods=["POST"])
def executeFromFile():
    try:
        fp = request.files["file"]   
        fileName = fp.filename
        tasks = request.form.to_dict()['tasks'].split(",")
        fileParts = fileName.split(".")
        newFileName = fileParts[0]+"_output."+fileParts[1]
        if fp:
            fp_opt = open("./output/" + newFileName, "w")
            n = 0
            m = 0
            days = []
            idx = 0
            while True:
                chunk = fp.readline().decode('utf-8').rstrip("\n ")
                if chunk == "":
                    break
                n = int(chunk)

                chunk = fp.readline().decode('utf-8').rstrip("\n ")
                if chunk == "":
                    break
                m = int(chunk)

                chunk = fp.readline().decode('utf-8').rstrip("\n ")
                if chunk == "":
                    break

                days = json.loads(chunk)
                days.sort()
                for task in tasks:
                    if task == '5':
                        continue
                    startTimer()
                    res = eval("TASK{0}.main(n, m, days)".format(task))
                    respData = {
                        "task": int(task),
                        "n": n,
                        "m": m,
                        "respLength": len(res),
                        "executionTime": returnExecutionTime(),
                    }

                    fp_opt.write(json.dumps(respData))
                    fp_opt.write("\n")
            fp_opt.close()

        return send_from_directory("./output/", newFileName, as_attachment=True)
    except Exception as e:
        print(e)
        return "Error occured"
