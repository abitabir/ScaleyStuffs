#!/bin/bash
MAX=300
for FILE in sample_processed.csv; do
gnuplot -p << EOF
set datafile separator ","
set xlabel "matrix size"
set xrange [10:$MAX]
set ylabel "program time"
set title "Execution time performance"
plot "$FILE" using 1:2 title "program time", \
     "$FILE" using 1:3 title "real time",\
     "$FILE" using 1:4 title "usr time",\
     "$FILE" using 1:5 title "sys time"

EOF
done