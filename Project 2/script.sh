#!/bin/bash

noOfTests=1

rm -rf plots/*
rm -rf input/* output/*
for ((x = 1; x <= $noOfTests; x++)); do
    m=8
    n=8
    h=5
    maxDiff=3
    testCases=1000
    task=1
    outputRespFolder="./plots/Plot$x/"

    make rungentest m=$m n=$n h=$h testcases=$testCases task=$task maxDiff=$maxDiff
    inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
    make runfromtestfile tasks="1,2,3" filename=$inpFileName
    make runfromtestfile tasks="4,5A,5B" filename=$inpFileName
    make runfromtestfile tasks="6,7A,7B" filename=$inpFileName
done
