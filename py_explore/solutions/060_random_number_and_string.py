#
## 60. Generate a random number (with 6 digits), string(alphanumeric with 8 chars width)
#

import random

## using choice() to generate a random number from a given list of numbers. 
print("A random number from list is : ", random.choice([1, 2, 5, 8, 10, 3]))

## using randrange() to generate in range from 20 to 50. '3' is step size.
print("A random number from range is : ", random.randrange(20, 50, 3))

## using random() to generate a random number between 0 and 1 
print("A random number between 0 and 1 is : ", random.random())

## using seed() to seed a random number
random.seed(5)
print ("The mapped random number with 5 is : ", random.random())

print("The original list is as below")
listx = [1, 2, 5, 8, 10, 3]
for li, le in enumerate( listx):
    print("Element @ listx[%d] is %d" % (li, le))

random.shuffle(listx)
print("****** After shuffling the list ******")

for li, le in enumerate( listx):
    print("Element @ listx[%d] is %d" % (li, le))

from random import choice
from string import ascii_lowercase

print(''.join(choice(ascii_lowercase) for i in range(8)))

from string import digits
print(''.join(choice(digits) for i in range(6)))


