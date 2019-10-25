#
## 13. Find factorial of a given number 1) Normal 2) Recursion
#

iter_value = number = int( input("Enter a number (> 0) to find factorial :"))
fvalue = 1
## TIP: while loop example
while iter_value > 1 :
    fvalue = fvalue * iter_value
    iter_value -= 1
print("Factorial of %d using 'while' loop is: %d" % (number, fvalue))

## TIP: Recursion example
def r_factorial(n):
    if ( n == 0):
        return n
    if ( n == 1):
        return 1
    else:
        return (n * r_factorial(n - 1))

print( "Factorial of %d using recursion is   : %d" % (number, r_factorial(number)))


