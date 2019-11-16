#
## 24. Check for EMail in a given string
#


import re

# Make a regular expression for validating an Email
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# Define a function for validating an Email
def check(email):

    # pass the regualar expression and the string in search() method
    if(re.search( regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


if __name__ == '__main__' :

    email = "vbhaskar_good@gmail.com"
    check(email)

    email = "my.ownsite@planetmars.org"
    check(email)

    email = "vbhaskar_bod.com"
    check(email)



