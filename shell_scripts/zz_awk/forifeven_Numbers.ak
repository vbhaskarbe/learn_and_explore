#!/bin/awk -f
#======================================================================
# AUTHOR      : Bhaskar.Varadaraju
# DATE        : 17th March 2006
# PROGRAM     : forifeven_Numbers.ak
# DESCRIPTION : This is an awk program to print even numbers 1 to 20.
#		A Demo program for - for and if in awk.
#=======================================================================
BEGIN {
	for ( Count = 1; Count <= 20; Count++) {
		if ( Count % 2 == 0)
			print "Even Number =",Count;
	}
	exit;
}

END {
  print "\nPrinted Even Numbers between 1 and 20";
}
