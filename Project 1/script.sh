#!/bin/bash

# minVal=1
# maxVal=1000
# testCases=1
# tasks=1,2,3,4
# highest=10000
# step=500

# i=1
# n=$((highest / step))

# rm input/* output/*
# for ((i = 1; i <= n; i++)); do
#     make rungentest minval=$minVal maxval=$maxVal testcases=$testCases
#     inpFileName=$(find ./input -printf '%T+ %p\n' | sort -r | head -n1 | awk '{print $2}' | awk -F '/' '{print $3}')
#     make runfromtestfile tasks=$tasks filename=$inpFileName
#     ((minVal += step))
#     ((maxVal += step))
# done

# make runplotoutput xaxis=n yaxis=m xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES" filename="./plots/Plot5/n_and_m.png"
# make runplotoutput xaxis=n yaxis=respLength xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES_PAINTED" filename="./plots/Plot5/n_and_respLength.png"
# make runplotoutput xaxis=n yaxis=executionTime xlabel="AVAILABILITY_OF_PAINTER" ylabel="EXECUTION_TIME" filename="./plots/Plot5/n_and_executionTime.png"

make rungentable
