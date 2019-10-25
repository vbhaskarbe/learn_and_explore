#
## 16. Environment variables in python: Print all key, values from environment. 
##     Check if a variable TEXT_DATA is set in environment, if so print its value.
#

import os

print('The environment variables are: ')
print(os.environ)

print( '#' * 75)
for key in os.environ.keys():
    print("Environment variable {} value is {}.".format( key, os.environ[key]))

print( '*' * 75)
if os.environ.get('TEXT_DATA'):
    print('ERROR: TEXT_DATA exists in the environment.')
else:
    print('INFO :TEXT_DATA does not exist in the environment.')
print( '~' * 75)


