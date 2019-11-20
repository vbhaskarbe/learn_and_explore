#!/usr/bin/perl 
# define array 
@rainbow = ("red", "green", "blue", "yellow", "orange", "violet", "indigo"); 
 
# extract elements 2 to 5 
# slice contains "blue", "yellow", "orange", "violet" 
@slice = @rainbow[2..5]; 
print "@slice\n";
#Done know the end element index? try this.
@slice = @rainbow[2..$#rainbow]; 
print "@slice\n";
