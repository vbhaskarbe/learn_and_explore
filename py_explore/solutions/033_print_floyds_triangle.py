#
## 33. Python program to print Floyds triangle
#

fend = 8
print("Print the Floyds triangle up to %d Rows" % fend)
numbers_per_row = inumber = 1
while fend > 0:
    count = 1
    while count <= numbers_per_row:
        print("%4d" % inumber, end='')
        count = count + 1
        inumber = inumber + 1
    print()
    numbers_per_row = count
    fend = fend - 1
