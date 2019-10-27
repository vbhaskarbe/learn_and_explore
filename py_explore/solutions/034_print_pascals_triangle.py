#
## 34. Python program to print Pascals triangle
#

prows = 9
print("The Pascals triangle up to %d Rows" % prows)

for row in range(0, prows):
    coff = 1
    for spaces in range(1, prows - row):
        print("  ", end="")

    for ptnum in range(0, row + 1):
        print("  ", coff, end="")
        coff = int(coff * (row - ptnum) / (ptnum + 1))
    print()


