#!/usr/bin/awk -f

{
  average = (($2 + $3 + $4) / (NF - 1))
  if ( average >= 80 )
        print $0,": A"
  else if ( (average >= 60) && (average < 80))
        print $0,": B"
  else if ( (average >= 50) && (average < 60))
        print $0,": C"
  else
        print $0,": FAIL"
}

