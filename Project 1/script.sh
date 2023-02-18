#!/bin/bash

minVal=1
maxVal=1000
testCases=20
tasks=1,2,3,4
highest=10000
step=1000

i=1
n=$((highest / step))

rm input/* output/*
for ((i = 1; i <= n; i++)); do
    make rungentest minval=$minVal maxval=$maxVal testcases=$testCases
    inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
    make runfromtestfile tasks=$tasks filename=$inpFileName
    ((maxVal += step))
done
make runplotoutput yaxis=respLength
