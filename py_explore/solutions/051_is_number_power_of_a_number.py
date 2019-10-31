#
## 51. Find whether a given number is a power of 4 or not
#

print("A Python program to find if a given number is power of another number")

number = int( input("Enter a number:"))
numpower = int( input("Enter a number for power:"))
start   = 1
pnumber = 0
while pnumber < number:
    pnumber = pow( start, numpower)
    #print(start, pnumber)
    if number == pnumber:
        print("YES. {} is a power of {}".format(number, numpower))
        break
    start = start + 1
if pnumber > number :
    print("No. {} is NOT a power of {}".format(number, numpower))

