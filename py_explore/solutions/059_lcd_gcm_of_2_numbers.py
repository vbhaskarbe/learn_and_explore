#
## 59. Write a python program to find LCM and GCD of two numbers?
#   LCD => Least Common Denominator
#   GCD => Greatest Common Divisor
#
print("This is a program to find LCM and GCD of 2 numbers")

def gcd(a, b):
    if( a == 0):
        return b
    return gcd( b % a, a)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def printSum(num1, den1,
                  num2, den2):

    # least common multiple
    # of denominators LCD
    # of 6 and 15 is 30.
    lcd = lcm(den1, den2);

    # Computing the numerators
    # for LCD: Writing 1/6 as
    # 5/30 and 7/15 as 14/30
    num1 *= (lcd / den1)
    num2 *= (lcd / den2)

    # Our sum is going to be
    # res_num/lcd
    res_num = num1 + num2;
    print( int(res_num) , "/" ,
                       int(lcd))

# Driver Code
# First fraction is 1/6
num1 = 1
den1 = 6

# Second fraction is 7/15
num2 = 7
den2 = 15
printSum(num1, den1, num2, den2);

