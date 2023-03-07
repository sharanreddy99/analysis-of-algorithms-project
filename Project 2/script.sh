#!/bin/bash

noOfTests=1

rm -rf plots/*
for ((x = 1; x <= $noOfTests; x++)); do
    m=25
    n=25
    h=10
    maxDiff=3
    testCases=8
    fixedAxis=("mn" "mk" "nk")
    variableAxis=("k" "n" "m")
    variableAxisLabels=("Faulty Plots" "No of Columns" "No of Rows")
    outputRespFolder="./plots/Plot$x/"

    for idx in {0..0}; do
        rm -rf input/* output/*
        make rungentest m=$m n=$n h=$h testcases=$testCases task=${fixedAxis[$idx]} maxDiff=$maxDiff
        inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
        make runfromtestfile tasks="1" filename=$inpFileName
        make runfromtestfile tasks="2,3" filename=$inpFileName
        make runfromtestfile tasks="4,5A,5B" filename=$inpFileName
        make runfromtestfile tasks="6,7A,7B" filename=$inpFileName
        make runplotoutput xaxis=${variableAxis[$idx]} yaxis=executionTime xlabel="${variableAxisLabels[$idx]}" ylabel="Execution Time" filename="${fixedAxis[$idx]}_${variableAxis[$idx]}_and_executionTime_1.png" foldername=${outputRespFolder} tasks="1"
        make runplotoutput xaxis=${variableAxis[$idx]} yaxis=executionTime xlabel="${variableAxisLabels[$idx]}" ylabel="Execution Time" filename="${fixedAxis[$idx]}_${variableAxis[$idx]}_and_executionTime_23.png" foldername=${outputRespFolder} tasks="2,3"
        make runplotoutput xaxis=${variableAxis[$idx]} yaxis=executionTime xlabel="${variableAxisLabels[$idx]}" ylabel="Execution Time" filename="${fixedAxis[$idx]}_${variableAxis[$idx]}_and_executionTime_45A5B.png" foldername=${outputRespFolder} tasks="4,5A,5B"
        make runplotoutput xaxis=${variableAxis[$idx]} yaxis=executionTime xlabel="${variableAxisLabels[$idx]}" ylabel="Execution Time" filename="${fixedAxis[$idx]}_${variableAxis[$idx]}_and_executionTime_67A7B.png" foldername=${outputRespFolder} tasks="6,7A,7B"
        make rungentable filename="table_${fixedAxis[$idx]}_${variableAxis[$idx]}_default.html" foldername=${outputRespFolder} tasks="1,2,3,4,5A,5B" testcases=$testCases
        make rungentable filename="table_${fixedAxis[$idx]}_${variableAxis[$idx]}_67.html" foldername=${outputRespFolder} tasks="6,7A,7B" testcases=$testCases
    done

    # make runmultiple tasks="4,5A,5B" m=$m n=$n h=$h testcases=$testCases task=$task maxDiff=$maxDiff
    # make runmultiple tasks="6,7A,7B" m=$m n=$n h=$h testcases=$testCases task=$task maxDiff=$maxDiff
done
