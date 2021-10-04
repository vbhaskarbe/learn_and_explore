#!/usr/local/bin/bash
#
# A Shell program to print 1 to 10 number using 'while'
#
count=1
while [ $count -le  10 ]
do
   echo $count
   count=`expr $count + 1`
done

