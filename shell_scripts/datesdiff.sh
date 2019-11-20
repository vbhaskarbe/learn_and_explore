#!/bin/bash
date1='Apr 08 2006 11:34:17'
date2='Apr 08 2006 13:35:19'

declare -a monthName 
declare -a monthNum 
monthName=(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec)
monthNum=(1 2 3 4 5 6 7 8 9 10 11 12)
monthDays=(31 28 31 30 31 30 31 31 30 31 30 31)
echo "monthName = ${monthName[*]}"
echo "monthNum = ${monthNum[*]}"
echo "monthDays = ${monthDays[*]}"

OLDIFS="$IFS"
IFS=' '
read month1 dat1 year1 tim1 <<<`echo $date1`
read month2 dat2 year2 tim2 <<<`echo $date2`
echo "$month1 $dat1 $year1 $tim1"
echo "$month2 $dat2 $year2 $tim2"
IFS=':'
read hr1 min1 sec1 <<<`echo $tim1`
read hr2 min2 sec2 <<<`echo $tim2`
echo "$hr1 $min1 $sec1"
echo "$hr2 $min2 $sec2"
IFS="$OLDIFS"
ressec=
let "ressec = sec2 - sec1"
echo "==>$ressec"
let "resmin = min2 - min1"
let "reshr = hr2 - hr1"
echo "Diff = $reshr:$resmin:$ressec"
