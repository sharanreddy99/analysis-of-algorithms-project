#!/bin/bash

noOfPlots=1
rm -rf plots/*

for ((x = 1; x <= $noOfPlots; x++)); do
    minVal=1
    testCases=1
    tasks=1,2,3,4,5
    highest=$((20000 * x))
    step=$((highest / 10))
    maxVal=$step
    outputRespFolder="./plots/Plot$x/"
    n=$((highest / step))

    rm -rf input/* output/*
    for ((i = 1; i <= n; i++)); do
        make rungentest minval=$minVal maxval=$maxVal testcases=$testCases n=$highest m=$maxVal task=4
        inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
        make runfromtestfile tasks=$tasks filename=$inpFileName
        ((maxVal += 1 * step))
    done

    make runplotoutput xaxis=m yaxis=executionTime xlabel="No of Houses" ylabel="Execution Time" filename="m_and_executionTime.png" foldername=${outputRespFolder} tasks=${tasks}
    make runplotoutput xaxis=m yaxis=respLength xlabel="No of Houses" ylabel="No of Houses Painted" filename="m_and_respLength.png" foldername=${outputRespFolder} tasks=${tasks}
    make rungentable filename="table.html" foldername=${outputRespFolder} tasks=${tasks}

done
