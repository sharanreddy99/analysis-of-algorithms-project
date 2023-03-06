#!/bin/bash

noOfTests=1

rm -rf plots/*
rm -rf input/* output/*
for ((x = 1; x <= $noOfTests; x++)); do
    m=20
    n=20
    h=5
    maxDiff=3
    testCases=100
    tasks=6,7A,7B
    task=1
    outputRespFolder="./plots/Plot$x/"

    make runmultiple tasks=$tasks m=$m n=$n h=$h testcases=$testCases task=$task maxDiff=$maxDiff

    # make rungentest m=$m n=$n h=$h testcases=$testCases task=$task maxDiff=$maxDiff
    # inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
    # make runfromtestfile tasks=$tasks filename=$inpFileName

done
