#
## 4. Program to find if a given number is prime?
#

import sys

if len(sys.argv) == 2:
    number = int(sys.argv[1])
else:
    number = int( input("Enter a number greater than 1: "))

# If num is divisible by any number between 2 and n / 2, it is not prime  
# TIP: Floor division operator is “//”, Integer round off.
for diviser in range(2, number // 1):
    if (number % diviser == 0):
        print( number, 'is NOT PRIME')
        exit(1)
print(number, 'is PRIME')

