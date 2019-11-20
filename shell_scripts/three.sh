#!/bin/bash

if [ $# -ne 3 ]
then
   echo "ERROR: Invalid arguments"
   echo "Info: $0 <highlim> <lowlim> <tagname>"
   exit
fi

SMALL=$1
BIG=$2
TAGNAME=$3
for num in `seq $SMALL $BIG`
do
  if [ $num -lt 100 ]
  then
     echo "runtest t_source:${TAGNAME}0${num} "
  else  
     echo "runtest t_source:${TAGNAME}${num} "
  fi
done
echo

