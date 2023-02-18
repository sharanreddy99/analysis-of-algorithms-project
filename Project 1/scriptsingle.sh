#!/bin/bash

plotName=testplot
outputRespFolder="./plots/$plotName/"
inpFileName=testcases_temp.txt
tasks=1,2,3,4

make runfromtestfile tasks=$tasks filename=$inpFileName
make runplotoutput xaxis=n yaxis=m xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES" filename="n_and_m.png" foldername=${outputRespFolder}
make runplotoutput xaxis=n yaxis=respLength xlabel="AVAILABILITY_OF_PAINTER" ylabel="NO_OF_HOUSES_PAINTED" filename="n_and_respLength.png" foldername=${outputRespFolder}
make runplotoutput xaxis=n yaxis=executionTime xlabel="AVAILABILITY_OF_PAINTER" ylabel="EXECUTION_TIME" filename="n_and_executionTime.png" foldername=${outputRespFolder}
make runplotoutput xaxis=m yaxis=executionTime xlabel="NO_OF_HOUSES" ylabel="EXECUTION_TIME" filename="m_and_executionTime.png" foldername=${outputRespFolder}
make runplotoutput xaxis=m yaxis=respLength xlabel="NO_OF_HOUSES" ylabel="NO_OF_HOUSES_PAINTED" filename="m_and_respLength.png" foldername=${outputRespFolder}
make rungentable filename="table.html" foldername=${outputRespFolder}
