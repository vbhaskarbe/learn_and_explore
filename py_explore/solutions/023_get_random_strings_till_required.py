#
## 23. Generating random strings until a given string is generated
#

import random
required_num = int( input("Enter a number between 2000-4000: "))
count = 0
while True:
    random_num = random.randint(2000, 4000)
    count     += 1
    print("Random number between 2000-4000 is: ", random_num)
    if required_num == random_num:
        print("The required random number '{}' is generated after {} iterations.".format(required_num, count))
        break

