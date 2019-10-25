#
## Program to print first 10 odd/even numbers?
#

import sys

if len(sys.argv) > 1:
    total = int(sys.argv[1])
else:
    total = int( input("Enter a positive number below 50: "))

## TIP: Initiaize multiple variable in one line using lists
oddcount, evencount = [ 0, 0 ] 
evenlist = []
oddlist  = []

## TIP: xrange() in 2.7 is now range() in 3.0+. range() from 2.7 is Removed.
for number in range(1, 1000):
    if ( number % 2 == 0):
        evenlist.append( number)
        evencount += 1
    else:
        oddlist.append( number)
        oddcount += 1
    ## TIP: break can be used to come out of a loop.
    if (evencount == total) and ( oddcount == total):
        break

print("The first {} EVEN numbers are: {}".format( total, evenlist))
print("The first {} ODD  numbers are: {}".format( total, oddlist ))

