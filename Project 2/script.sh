#!/bin/bash

noOfTests=2

rm -rf plots/*
rm -rf input/* output/*
for ((x = 1; x <= $noOfTests; x++)); do
    m=15
    n=15
    h=10
    maxDiff=3
    testCases=50
    fixedAxis=("mn" "mk" "nk")
    variableAxis=("k" "n" "m")
    variableAxisLabels=("Faulty Plots" "No of Columns" "No of Rows")
    outputRespFolder="./plots/Plot$x/"

    for idx in {0..2}; do
        make rungentest m=$m n=$n h=$h testcases=$testCases task=${fixedAxis[$idx]} maxDiff=$maxDiff
        inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
        make runfromtestfile tasks="1,2,3" filename=$inpFileName
        make runfromtestfile tasks="4,5A,5B" filename=$inpFileName
        make runfromtestfile tasks="6,7A,7B" filename=$inpFileName
        make runplotoutput xaxis=${variableAxis[$idx]} yaxis=executionTime xlabel="${variableAxisLabels[$idx]}" ylabel="Execution Time" filename="${fixedAxis[$idx]}_${variableAxis[$idx]}_and_executionTime_123.png" foldername=${outputRespFolder} tasks="1,2,3"
        make runplotoutput xaxis=${variableAxis[$idx]} yaxis=executionTime xlabel="${variableAxisLabels[$idx]}" ylabel="Execution Time" filename="${fixedAxis[$idx]}_${variableAxis[$idx]}_and_executionTime_45A5B.png" foldername=${outputRespFolder} tasks="4,5A,5B"
        make runplotoutput xaxis=${variableAxis[$idx]} yaxis=executionTime xlabel="${variableAxisLabels[$idx]}" ylabel="Execution Time" filename="${fixedAxis[$idx]}_${variableAxis[$idx]}_and_executionTime_67A7B.png" foldername=${outputRespFolder} tasks="6,7A,7B"
        # make rungentable filename="table.html" foldername=${outputRespFolder} tasks=${tasks}
    done

    # make runmultiple tasks="4,5A,5B" m=$m n=$n h=$h testcases=$testCases task=$task maxDiff=$maxDiff
    # make runmultiple tasks="6,7A,7B" m=$m n=$n h=$h testcases=$testCases task=$task maxDiff=$maxDiff
done
