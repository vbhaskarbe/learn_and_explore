
#
## A Python program to learn command line arguments in Python
# 
# ToDo: Explore argparse?
# 
import sys

print("The total number of command line arguments : ", len(sys.argv))
print("First argument is                          : ", sys.argv[0])
print("Last argument is                           : ", sys.argv[-1])
print("All the command line arguments are         : ", sys.argv)
print("The arguments to the program are           : ", sys.argv[1::])
print("The reversed command line arguments are    : ", sys.argv[::-1])
print("All the command line arguments one/line    : ")

for dataitem in sys.argv:
    print(dataitem)


