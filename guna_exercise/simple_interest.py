"""
formula for simple interest PTR/100

"""
from builtins import input
principal_amount = int(input("enter principal amount: "))
time = int(input("enter the duration: "))
rate = int(input("enter rate of interest: "))

total = principal_amount*time*rate/100
print(f'simple interest:', total)