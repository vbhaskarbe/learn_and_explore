#!/bin/bash
if test $# -gt 9
then 
  echo "The 10th argument is ${10}"
  echo "The 11th argument is ${11}"
else
   echo "arguments are less than 10"
fi
