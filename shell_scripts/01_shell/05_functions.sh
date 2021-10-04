#!/usr/local/bin/bash
# Author: Bhaskar Varadaraju
#
# A Shell program to compute factorial of given number using function
#

factorial ()
{
	num1=$1
	fsum=1
	while [ $num1 -gt 1 ]
	do
		fsum=`expr $fsum \* $num1`
   		num1=`expr $num1 - 1`
	done
	#echo $fsum
	return $fsum
}
#result=`factorial "5"`
factorial "5"
echo "The factorial of 5 is: $?"

