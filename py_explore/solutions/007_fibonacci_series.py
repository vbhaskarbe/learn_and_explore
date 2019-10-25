#
##  Write a python program to print Fibonacci series (up to 500)?
#	a) print first ’n’ numbers of fibonacci series?
#	b) Is given number a part of fibonacci series?
#   1 1 2 3 5 8 13 21 34 
#
fnumber = int(input("Enter a a number below 100000: "))
if fnumber > 100000:
    print( fnumber, 'is greater than 100000')
    exit(1)

startf    = 0
nextf     = 1
fibonacci = 1
LIMIT     = 100000
fcount    = 0
print("The first {} fibonnaci numbers are: ")
while nextf < LIMIT:
    fibonacci = nextf
    if fcount < fnumber:
        print( fibonacci, end=' ')
        fcount += 1
    nextf  = fibonacci + startf
    startf = fibonacci
print()

fnumber = int(input("Enter a a number below 100000: "))
if fnumber > 100000:
    print( fnumber, 'is greater than 100000')
    exit(1)

startf    = 0
nextf     = 1
fibonacci = 1
LIMIT     = 100000
while nextf < LIMIT:
    fibonacci = nextf
    if fnumber == fibonacci:
        print(fnumber, 'is a Fibonacci number')
        break
    nextf  = fibonacci + startf
    startf = fibonacci
if nextf > LIMIT:
    print(fnumber, 'is NOT a Fibonacci number')


