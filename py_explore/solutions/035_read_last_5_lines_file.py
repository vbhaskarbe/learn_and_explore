#
# 35. Write a Python program to read last n lines of a file
#

import sys

try:
    fl_handle = open( sys.argv[0], 'r')
    all_lines = []
    for line in fl_handle:
        all_lines.append( line)
    fl_handle.close()
except Exception as e:
    print("ERROR: ", e)
finally:
    print("The last 5 lines in the file are: ", sys.argv[0], len(all_lines))
    for line in (all_lines[-5::]) :
        print(line, end='')

#Last line 5
#Last line 4
#Ths is the last line 3
#The is last but one line
#Finally this is the last of this file.
