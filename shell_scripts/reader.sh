#!/bin/bash
echo "Enter a value?"
read a
echo $a
read -p "Enter a value?" a
echo $a
read -p "Enter [y/n]?" -n 1 a
echo $a
read -p "Enter a 8 char password?" -n 8 -s a
echo
read -p "Enter a value having ' ' TAB newlines, end with :" -d : a
echo "val1=$a"
read -p "Enter a 8 char password in withing 5 seconds?" -t 5 -s tm
echo $tm

