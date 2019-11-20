#! /bin/sh
echo -ne "\n\tEnter Something : "
read Text
echo -n "The Something Reversed is : "
echo "$Text" | sed ' s/\(.*\)/!\1!/
		    :a
		    s/!\(.\)\(.*\)\(.\)!/\3!\2!\1/
		    ta
		    s/!//g '
