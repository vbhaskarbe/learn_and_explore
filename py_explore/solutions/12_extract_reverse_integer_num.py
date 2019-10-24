#
## 12. Python program to extract and print digits in reverse order of a number
#

number = input("Enter a positive integer: ")

rev_number = 0
len_number = len(number)
number     = int(number)

for count in range(0, len_number):
    rev_number = (rev_number * 10) + (number % 10)
    number     = number // 10

print(f"The number reversed is  : %0*d" % (len_number, rev_number))

