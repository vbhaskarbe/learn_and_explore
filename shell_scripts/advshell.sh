#!/bin/bash

myarray=("my name" "your name" 10 "what is your name" 20 end ) 
echo "myarray = ${myarray[@]}"

myfunc1 () {
  arrName=$1
  arrCount=$2
  echo "arrName = $arrName"
  echo "arrCount = $arrCount" 
  index=0
  while [ $index -lt $arrCount ]
  do
     eval echo \${$arrName[$index]}
     let "index = $index + 1"
  done
}

myfunc1 myarray ${#myarray[*]}
#funcName arrName numArgs
