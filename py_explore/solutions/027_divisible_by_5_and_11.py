#
## 27. Check if a number if divisible by 5 and also 11
#

number = int( input("Enter a positive number: "))

if ( ( number % 5 == 0 ) and (number % 11 == 0)):
    print("Number {} is divisible by 5 and 11.".format(number))
else:
    print("Number {} is NOT divisible by 5 and 11.".format(number))


