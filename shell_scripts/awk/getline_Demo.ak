#!/bin/awk -f
#======================================================================
# AUTHOR      : Bhaskar.Varadaraju
# DATE        : 17th March 2006
# PROGRAM     : getline_Demo.ak
# DESCRIPTION : This is an awk program to read user input.
#=======================================================================
BEGIN {
	print "Enter your name?";
	getline name < "-"
	print "Hi,", name"! Welcome to Awk";
	exit ;
}
