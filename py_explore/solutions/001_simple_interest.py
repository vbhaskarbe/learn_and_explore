
"""
1. Write a Python program to calculate simple interest?
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principal amount
T is the time and
R is the rate of interest
"""

import sys

PROGRAM_NAME = sys.argv[0]
## TIP - Checking for required program arguments
if len(sys.argv) < 4:
    print('ERROR: 3 Arguments are required for this program.')
    ## TIP - Formatted output using 'format'
    print("USAGE: python {} <P> <T> <R>".format(PROGRAM_NAME))
    print('       where,')
    print('         P is the principal amount in rupees')
    print('         T is the time duration of loan in years')
    print('         R is the rate of interest per year')
    print("EXAMPLE: python {} 100000 3.0 24".format(PROGRAM_NAME))
    exit(1)

principal_amount = float(sys.argv[1])
time_in_years    = float(sys.argv[2])
rate_of_interest = float(sys.argv[3])

simple_interest = (principal_amount * time_in_years * rate_of_interest) / 100

## TIP - Justified output using % notation
print("Principal amount is: %10.2f" % principal_amount)
print("Time duration is   : %10.2f" % time_in_years)
print("Rate of interest is: %10.2f" % rate_of_interest)
print("Simple interest is : %10.2f" % simple_interest)


