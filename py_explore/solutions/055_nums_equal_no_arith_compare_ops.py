#
## 55. Check if two numbers are equal without using arithmetic and comparison operators. (Use bit wise operators)
#

number1 = 21
number2 = 20
number3 = 21

## TIP: num1 XOR num2 == 0, then they are equal
print(number1 ^ number2)
print(number1 ^ number3)
## TIP: num1 AND (COMPLIMENT num2) == 0, then they are equal
print(number1 & ~number2)
print(number1 & ~number3)


