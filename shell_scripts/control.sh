#!/bin/bash
for a in 10 20
do
   # Instead of 
   if [ $a -eq 10 ]
   then
       echo "a Equals 10"
   else
       echo "a is not Equal to 10"
   fi
   #Use
   [ $a -eq 10 ] && echo "a Equals 10" || echo "a is not Equal to 10"
done
      
