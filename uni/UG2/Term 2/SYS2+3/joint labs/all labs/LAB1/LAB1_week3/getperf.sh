#!/bin/bash
MIN=10
MAX=50
STEP=10
COUNT=$MIN
LineCount=1
matrix=()
writematrix=()
file=./data.txt
if [ -f "$file" ]; then
  rm $file
fi

while [ $COUNT -le $MAX ]; do
	(/usr/bin/time  ./mmp $COUNT ) >> data.txt 2>&1	
	let COUNT=COUNT+STEP
done
