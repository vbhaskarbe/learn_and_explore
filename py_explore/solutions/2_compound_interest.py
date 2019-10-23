
"""
2. Write a Python program to calculate compound interest?
Formula to calculate compound interest annually is given by:
Compound Interest = P(1 + R/100)r
    Where,
        P is principle amount
        R is the rate and
        T is the time span
"""
import sys

if len(sys.argv) < 4:
    print("Minimum 3 arguments needs to be given via CLI")
    exit(1)

principal_amount  = float(sys.argv[1])
rate_of_interest  = float(sys.argv[2])
time_span_of_loan = float(sys.argv[3])

compound_amount = principal_amount * ( pow( (1 + (rate_of_interest / 100)), time_span_of_loan))
print("The principal amount is  : %10.2f" % round(principal_amount))
print("The rate of interest is  : %10.2f" % rate_of_interest)
print("The time span of loan is : %10.2f" % time_span_of_loan)
print("The compound amount is   : %10.2f" % round(compound_amount, 2))
print("The compound interest is : %10.2f" % round(compound_amount - principal_amount,2))



