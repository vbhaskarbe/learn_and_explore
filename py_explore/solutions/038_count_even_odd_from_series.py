#
## 38. Write a Python program to count the number of even and odd numbers from a series of numbers
#

num_series   = [ 100, 33, 11, 9, 12, 46, 59, 28, 91, 43, 60, 84 ]
odd_numbers  = list( filter( lambda x: (x % 2 == 1), num_series))
even_numbers = list( filter( lambda y: (y % 2 == 0), num_series))
print("The series of numbers are         :", num_series)
print("The odd numbers in the series are :", odd_numbers)
print("The even numbers in the series are:", even_numbers)


