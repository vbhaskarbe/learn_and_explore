#!/usr/bin/awk -f

{
  if ( NR % 2 == 1 ) {
        ORS=";";
  } else {
        ORS="\n";
  }
  print $0
}
