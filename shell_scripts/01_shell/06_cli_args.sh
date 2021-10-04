#!/usr/local/bin/bash
# A Shell program to check and print cli arguments passed (positional params)
# Usage: bash 06_cli_args.sh ab cd ef gh ij kl mn op qr st uv
# Also, Try  : 
#	bash 06_cli_args.sh
# 	bash 06_cli_args.sh ab
# 	bash 06_cli_args.sh ab cd
# 
test $# -ge 2 && \
	echo “INFO: Received required arguments” || \
	{ echo “ERROR: At least 2 arguments must be passed at cli”; exit 1; }

echo “This scripts name is          : $0”  # 06_cli_args.sh
echo “The first argument is         : $1”
echo “The number of arguments is    : $#”
echo “The list of arguments passed1 : $@”
echo "The list of arguments passed2 : $*"  # Difference between '$*' and '$@'??
echo “The exit status of last cmd   : $?”
echo "The last argument at cli is   : ${!#}"
echo “This script process id 	    : $$”
echo "The 10th cli arguments is     : ${10}"
# NOTE: If CLI arguments are more than 9 then use ${} notation.
# Example : To print 10th cli arguments use ${10} as $10 does not work.
######## Sample Run ########
# $ bash 06_cli_args.sh ab cd ef gh ij kl mn op qr st uv 
# “INFO: Received required arguments”
# “This scripts name is : 06_cli_args.sh”
# “The first argument is : ab”
# “The number of arguments is : 11”
# “The list of arguments passed1 : ab cd ef gh ij kl mn op qr st uv”
# The list of arguments passed2 : ab cd ef gh ij kl mn op qr st uv
# “The exit status of last cmd : 0”
# The last argument at cli is   : uv
# “This script process id : 73971”
# The 10th cli arguments is     : st

