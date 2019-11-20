#!/bin/bash

if [ $# -ne 3 ]
then
   echo "ERROR: Invalid arguments"
   echo "Info: $0 <highlim> <lowlim> <tagname>"
   exit
fi

BIG=$1
SMALL=$2
TAGNAME=$3
for num in `seq $BIG $SMALL`
do
  if [ $num -lt 100 ]
  then
     echo -n "${TAGNAME}0${num}.tsc "
  else  
     echo -n "${TAGNAME}${num}.tsc "
  fi
done
echo

