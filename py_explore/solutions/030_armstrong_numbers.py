#
## 30. Print first 5 Armstrong number from 100
#

#! ---------------------------------------------------------------
#! This program computes all Armstrong numbers in the range of
#! 0 and 999.  An Armstrong number is a number such that the sum
#! of its digits raised to the third power is equal to the number
#! itself.  For example, 371 is an Armstrong number, since
#! 3**3 + 7**3 + 1**3 = 371.
#! ---------------------------------------------------------------

arms  = 10
print("The first %2d armstrong numbers starting from 100 are: " % arms)
count = 0
start = 100
while count < arms:
    number = anumber = start
    pow_factor = len( str(anumber))
    start  = start + 1
    sum_digits = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        sum_digits = sum_digits + pow( digit, pow_factor)
    if anumber == sum_digits:
        count = count + 1
        print("Armstrong number %2d is %d" % ( count, anumber))


