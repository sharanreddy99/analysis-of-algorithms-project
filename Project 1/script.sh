#!/bin/bash

noOfPlots=30

for ((x = 1; x <= $noOfPlots; x++)); do
    minVal=1
    maxVal=1000
    testCases=1
    tasks=1,2,3,4
    highest=10000
    step=500
    outputRespFolder="./plots/Plot$x/"
    n=$((highest / step))

    rm input/* output/*
    for ((i = 1; i <= n; i++)); do
        make rungentest minval=$minVal maxval=$maxVal testcases=$testCases
        inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
        make runfromtestfile tasks=$tasks filename=$inpFileName
        ((maxVal += step))
    done

    make runplotoutput xaxis=n yaxis=m xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES" filename="n_and_m.png" foldername=${outputRespFolder}
    make runplotoutput xaxis=n yaxis=respLength xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES_PAINTED" filename="n_and_respLength.png" foldername=${outputRespFolder}
    make runplotoutput xaxis=n yaxis=executionTime xlabel="AVAILABILITY_OF_PAINTER" ylabel="EXECUTION_TIME" filename="n_and_executionTime.png" foldername=${outputRespFolder}
    make runplotoutput xaxis=m yaxis=executionTime xlabel="NO_OF_HOUSES" ylabel="EXECUTION_TIME" filename="m_and_executionTime.png" foldername=${outputRespFolder}
    make runplotoutput xaxis=m yaxis=respLength xlabel="NO_OF_HOUSES" ylabel="NO_OF_HOUSES_PAINTED" filename="m_and_respLength.png" foldername=${outputRespFolder}
    make rungentable filename="table.html" foldername=${outputRespFolder}

done
