#
## 37. Write a Python program to count the number of lines in a text file. 
#

import sys
filename   = sys.argv[0]
line_count = 0
try:
    fh = open( filename, 'r')
    for line in fh:
        line_count = line_count + 1
    fh.close()
except Exception as e:
    print("Error: ", e)
finally:
    print("The number of lines in {} is {}".format( filename, line_count))


