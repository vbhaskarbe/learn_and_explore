#
## 15. Common line arguments to python: Print count, list them, print the last argument value.
#

import sys

print("The count of command line arguments is : ", len(sys.argv))
print("The command line arguments given are   : ", sys.argv)
print("The last command line argument is      : ", sys.argv[-1])
print("The command line arguments reversed is : ", sys.argv[::-1])
print("The name of this python program is     : ", sys.argv[0])
print("The actual arguments to the program are: ", sys.argv[1::])


