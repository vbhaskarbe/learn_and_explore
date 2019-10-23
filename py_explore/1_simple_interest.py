
"""
1. Write a Python program to calculate simple interest?
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate of interest
"""

import sys
if len(sys.argv) < 3:
    print('3 Arguments are required for this program.')
    ## TIP - Formatted output using 'format'
    print("USAGE: {} <P> <T> <R>".format(sys.argv[0]))
    print('      where,')
    print('         P is the principle amount in rupees')
    print('         T is the time of loan in years')
    print('         R is the rate of interest per year')
    exit(1)

principle_amount = float(sys.argv[1])
time_in_years    = float(sys.argv[2])
rate_of_interest = float(sys.argv[3])

simple_interest = (principle_amount * time_in_years * rate_of_interest) / 100

## TIP - Justified output using % notation
print("Principle amount is: %10.2f" % principle_amount)
print("Time duration is   : %10.2f" % time_in_years)
print("Rate of interest is: %10.2f" % rate_of_interest)
print("Simple interest is : %10.2f" % simple_interest)


