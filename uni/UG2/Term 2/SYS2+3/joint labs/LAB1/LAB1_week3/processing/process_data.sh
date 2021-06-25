input="./sample_data.txt"
while IFS= read -r line
do
  let rem=($LineCount%2)
  newline=$(echo $line | tr -d  s) 
  matrix+=($newline)
  if [ $rem -eq 1 ]; then
     writematrix+=(${matrix[1]})
  else
   writematrix+=(${matrix[1]})
   writematrix+=(${matrix[2]})
   writematrix+=(${matrix[4]})
   writematrix+=(${matrix[6]})
   echo ${writematrix[0]}","${writematrix[1]}","${writematrix[2]}","${writematrix[3]}","${writematrix[4]} >> processed.csv
   writematrix=()
  fi 
  matrix=()
  let LineCount=LineCount+1
done < "$#
input"
