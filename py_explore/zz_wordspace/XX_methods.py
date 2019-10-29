

def my_print():
    print("Hello World!")

def name_print( name = 'Bhaskar'):
    print(name, "Good Morning!")

def number_odd_even( num):
    if num % 2 == 0:
        print(num, "is Even number")
    else:
        print(num, "is Odd number")

def sum_of_2_nums(m, n):
    sum = m + n
    print( "Sum of {} and {} is {}".format(m, n, sum))

def sum_of_many_numbers( *numbers):
    """docstring - 'sum_of_many_numbers' is method to demonstrate variable arguments"""
    sum = 0
    for number in numbers:
        sum = sum + number
    print("Sum of all numbers {} is: {}".format(list(numbers), sum))

def thisGenerator():
    mylist = range(1,10)
    for number in mylist:
        yield number * number

def use_kwargs( **kwargs):
    for key, value in kwargs.items():
        print( "%s ==> %s" % (key, value))

my_print()
name_print()
name_print('Lehit')
number_odd_even( 11)
sum_of_2_nums(10, 19)
nums = ( 20, 30)
sum_of_2_nums( *nums)
print(sum_of_many_numbers.__doc__)
sum_of_many_numbers(10)
sum_of_many_numbers(12, 14)
sum_of_many_numbers(16, 18, 20)
sum_of_many_numbers(1, 2, 10, 11, 7, 9, 3)
for gen in thisGenerator():
    print( gen)

use_kwargs( name = 'Bhaskar', profession = 'Software', salary = 'Unknown')
use_kwargs( first = 'Lehit', second = 'Is', third = 'a', fourth = 'Good', fifth = 'Boy')

