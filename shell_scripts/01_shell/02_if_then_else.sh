#!/usr/local/bin/bash
# Author: Bhaskar Varadaraju
#
# A Shell program to check given number is positive or negative.
#
read -p "Enter number : " num
if test $num -ge 0
then
	echo "$num is positive number."
else
	echo "$num number is negative number."
fi


