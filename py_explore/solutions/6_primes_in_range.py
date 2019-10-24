#
## 6. Program to print prime numbers between given range?
#

import sys

if len(sys.argv) < 3:
    print("ERROR: {} required minimum 2 arguments, start, end numbers", sys.argv[0])
    exit(1)

start = int(sys.argv[1])
end   = int(sys.argv[2])

primes_list = []
# Generate numbers in given range
for number in range( start, end):
    half = number // 2
    for diviser in range( 2, half):
        if number % diviser == 0:
            break
    if (diviser == (half - 1)):
        primes_list.append(number)

if (len(primes_list) == 0 ):
    print("The primes numbers between {} and {} are: None".format( start, end))
else:
    print("The primes numbers between {} and {} are: {}".format( start, end, primes_list))

            
