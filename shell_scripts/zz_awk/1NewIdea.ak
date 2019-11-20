#!/bin/awk -f 

BEGIN {
   n=1000
} 

{
   $3 = n - $3;
}
2
