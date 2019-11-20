#!/bin/awk -f
#======================================================================
# AUTHOR      : Bhaskar.Varadaraju
# DATE        : 17th March 2006
# PROGRAM     : userdef_Funcs.ak
# DESCRIPTION : This is an demo awk program using user defined functions
#		in awk.
#=======================================================================
function mesg_Display(Str) {
	print "Info:",Str;
}
BEGIN {
	mesg_Display("Oracle India Private Limited.");
	exit;
}
