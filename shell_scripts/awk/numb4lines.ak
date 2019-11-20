#!/bin/awk f

BEGIN { 
printf("Line numbers by awk\n");
}

{ 
printf("%d: %s\n",NR,$0); 
printf("%d: %s\n",FNR,$0); 
}

