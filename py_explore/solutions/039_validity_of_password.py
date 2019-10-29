#
## 39. Write a Python program to check the validity of password input by users. (
#    1. At least 1 letter between [a-z] and 1 
#       letter between [A-Z], 
#       At least 1 number between [0-9], 
#       At least 1 character from [_$#@], 
#       Minimum length 6 characters, 
#       Maximum length 16 characters
#

vpassword = input('Enter a password : ')
VALIDPASS = True

if len(vpassword) < 6:
    print('ERROR: Length should be atleast 6')
    VALIDPASS = False

if len(vpassword) > 16: 
    print('ERROR: Length should be at max 16')
    VALIDPASS = False
    
if not any( char.isdigit() for char in vpassword):
    print('ERROR: Password should have atleast one numberal')
    VALIDPASS = False

if not any( char.isupper() for char in vpassword):
    print('ERROR: Password should have atleast one upper case letter')
    VALIDPASS = False

if not any( char.islower() for char in vpassword):
    print('ERROR: Password should have atleast one lower case letter')
    VALIDPASS = False

special_chars =['$', '@', '#', '_']
if not any(char in special_chars for char in vpassword):
    print('ERROR: Password should have at least one of the symbols \'_$#@\'')
    VALIDPASS = False

if VALIDPASS :
    print('\'{}\' is a Valid password'.format( vpassword))
else:
    print('\'{}\' is not a Valid password'.format( vpassword))

