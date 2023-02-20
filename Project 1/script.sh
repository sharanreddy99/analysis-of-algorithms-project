#!/bin/bash

noOfPlots=10
rm -rf plots/*

for ((x = 1; x <= $noOfPlots; x++)); do
    minVal=1
    maxVal=10000
    testCases=15
    tasks=2,3,4
    highest=10000
    step=10000
    outputRespFolder="./plots/Plot$x/"
    n=$((highest / step))

    rm -rf input/* output/*
    for ((i = 1; i <= n; i++)); do
        make rungentest minval=$minVal maxval=$maxVal testcases=$testCases task=3
        inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
        make runfromtestfile tasks=$tasks filename=$inpFileName
        ((maxVal += step))
    done

    make runplotoutput xaxis=n yaxis=m xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES" filename="n_and_m.png" foldername=${outputRespFolder} tasks=${tasks}
    make runplotoutput xaxis=n yaxis=respLength xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES_PAINTED" filename="n_and_respLength.png" foldername=${outputRespFolder} tasks=${tasks}
    make runplotoutput xaxis=n yaxis=executionTime xlabel="AVAILABILITY_OF_PAINTER" ylabel="EXECUTION_TIME" filename="n_and_executionTime.png" foldername=${outputRespFolder} tasks=${tasks}
    make runplotoutput xaxis=m yaxis=executionTime xlabel="NO_OF_HOUSES" ylabel="EXECUTION_TIME" filename="m_and_executionTime.png" foldername=${outputRespFolder} tasks=${tasks}
    make runplotoutput xaxis=m yaxis=respLength xlabel="NO_OF_HOUSES" ylabel="NO_OF_HOUSES_PAINTED" filename="m_and_respLength.png" foldername=${outputRespFolder} tasks=${tasks}
    make rungentable filename="table.html" foldername=${outputRespFolder} tasks=${tasks}

done
