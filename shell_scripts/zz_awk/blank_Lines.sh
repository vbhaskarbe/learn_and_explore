#!/bin/bash					
#======================================================================
# AUTHOR      : Bhaskar.Varadaraju
# DATE        : 17th March 2006
# PROGRAM     : blank_Lines.sh
# DESCRIPTION : This is an awk program to print number of blank lines
#               in a given input file.
#======================================================================= 
			
awk 'BEGIN { count = 0 }
     /^[	 ]*$/ { count++ }
     END { print "There are",count, "blank lines in file \"",FILENAME,"\""}' $1

