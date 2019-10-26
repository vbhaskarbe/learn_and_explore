#
## 29. Print multiplication table for given number
#

number = int( input("Enter a number below 25: "))
print("The multiplication table for", number, "is")
for count in range(1,21,1):
    print("%8d * %2d = %3d" % (number, count, number * count))

