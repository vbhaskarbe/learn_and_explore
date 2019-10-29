

num_list = [ 10, 11, 12, 13, 14, 15, 19,18, 16 ]

import time

# List Comprehension
print( [ x for x in num_list if x % 2 == 0])

# Generator
for gen in (x for x in num_list if x % 2 == 0):
    print (gen, end=' ')
print()


