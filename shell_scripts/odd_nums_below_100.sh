

for number in `seq 99`
do
   result=$((number % 2))
   if [ $result -eq 1 ]
   then
     echo $number
   fi
done
