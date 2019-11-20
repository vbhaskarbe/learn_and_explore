#!/bin/bash
var1=10
# DEBUG BLOCK
echo "Hello, World!"
last_cmd_arg=$_
echo "At line no $LINENO, var1 = $var1"
echo "Last command argument processed is $last_cmd_arg"
echo "LINENO = $LINENO, BASH_FUNCNAME = ${FUNCNAME[*]}, BASH_SOURCE = ${BASH_SOURCE[0]}"
echo "BASH_COMMAND = $BASH_COMMAND"
echo "FUNCNAME = ${FUNCNAME[*]}"
echo "TOTAL FUNCs = ${#FUNCNAME[*]}"

myfunc () {
last_cmd_arg=$_
  echo "Hello, $1"
echo "At line no $LINENO, var1 = $var1"
echo "Last command argument processed is $last_cmd_arg"
echo "BASH_LINENO = ${BASH_LINENO[0]}, BASH_FUNCNAME = ${FUNCNAME[0]}, BASH_SOURCE = ${BASH_SOURCE[0]}"
echo "Current Command is = $BASH_COMMAND"
echo "FUNCNAME = ${FUNCNAME[*]}"
echo "TOTAL FUNCs = ${#FUNCNAME[*]}"
}
var1=20
echo;
myfunc Bhaskar
echo
trap '' DEBUG
var1=
trap 'echo "Value of var1 = $var1"' DEBUG
var1=10
var1=20
var1=30

n="-n"
echo $n
