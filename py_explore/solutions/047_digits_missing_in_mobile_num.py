#
## 47. Write a Python program to find the digits which are absent in a given mobile number.
#

mnumber = input("Enter a mobile number (10 digits): ")
digits  = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
nlist   = set([digit for digit in mnumber])
print("The missing digits in mobile number %s are : %s" % (mnumber, digits - nlist))


