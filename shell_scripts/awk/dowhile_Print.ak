#!/bin/awk -f
#======================================================================
# AUTHOR      : Bhaskar.Varadaraju
# DATE        : 17th March 2006
# PROGRAM     : dowhile_Print.ak
# DESCRIPTION : This is an awk program to print Oracle 10 times
#		A Demo program for do-while loop in awk.
#=======================================================================
BEGIN {
	Count = 1;
	do {
		print "Oracle";
		Count++;
	} while (Count <= 10 );
	exit;
}
