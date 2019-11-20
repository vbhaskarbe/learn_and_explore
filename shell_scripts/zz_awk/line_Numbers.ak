#!/bin/awk -f
#======================================================================
# AUTHOR      : Bhaskar.Varadaraju
# DATE        : 17th March 2006
# PROGRAM     : line_Numbers.ak
# DESCRIPTION : This is an awk program to print the line number at the
#               begining of each line.
#=======================================================================
BEGIN {
	printf("Line Numbers by awk\n");
}
{
	printf("%d: %s\n",NR,$0);
}
