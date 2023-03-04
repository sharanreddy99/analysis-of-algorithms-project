import time

startTime = None
endTime = None


def startTimer():
    global startTime
    startTime = time.time()


def returnExecutionTime():
    global endTime
    endTime = time.time()
    return endTime - startTime
