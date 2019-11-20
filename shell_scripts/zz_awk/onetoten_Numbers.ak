#!/bin/awk -f
#======================================================================
# AUTHOR      : Bhaskar.Varadaraju
# DATE        : 17th March 2006
# PROGRAM     : onetoten_Numbers.ak
# DESCRIPTION : This is an awk program to print numbers 1 to 10.
#		A Demo program for while loop in awk.
#=======================================================================
BEGIN { 
	Count = 1;
	while ( Count <= 10 ) {
		print "Count =", Count;
		Count++;
	}
	exit;
}
