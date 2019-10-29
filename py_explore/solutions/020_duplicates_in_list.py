#
## 20. Python Program to print duplicates from a list of integers
#

import time
start_time = time.time()

listorig1   = [ 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50, 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50, 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50, 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50,50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50, 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50, 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50,50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50 ]
#listorig1   = [ 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50 ]
#listorig1   = [ 1, 2, 9, 4, 5, 6, 7, 8, 3 ]
#listorig1   = [ 1, 2, 2 ]
listdup1    = []
listnondup1 = []
print("Elements in the original list1 are     :", listorig1)

listorig1.sort()
print("Elements list after sorting is         :", listorig1)

index  = 0
length = len( listorig1)
while index < length:
    sindex = index + 1
    while sindex < length:
        if listorig1[index] != listorig1[sindex]:
            break
        else:
            sindex += 1
    if (index != (sindex - 1)):
        listdup1.append(listorig1[index])
    else:
        listnondup1.append(listorig1[index])
    index = sindex
print("The duplicate elements in listorig1 are:", listdup1)
print("The unique elements in listorig1 are   :", listnondup1)

print("--- %s seconds ---" % (time.time() - start_time))

## Simpler and Fasterway.   Above logic takes 7sec. But below logic takes 3sec.
## TIP: Use list comprehension, and also built-ins where available.
start_time = time.time()
listorig1   = [ 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40, 50 ]
print("The duplicate elements in listorig1 are:", set([num for num in listorig1 if listorig1.count(num) > 1]))
print("The unique elements in listorig1 are   :", set([num for num in listorig1 if listorig1.count(num) == 1]))

print("--- %s seconds ---" % (time.time() - start_time))
