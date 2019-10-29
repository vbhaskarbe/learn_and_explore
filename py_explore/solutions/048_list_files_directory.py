#
## 48. Write a Python program to list all files in a directory in Python. 
#

import os

cwd = os.getcwd()
print("The list of files in folder '{}' are:".format(cwd))
for entry in os.listdir(cwd):
    if os.path.isfile(cwd+'/'+entry):
        print(cwd+'/'+entry)
    else:
        print(cwd+'/'+entry, "is NOT a File <======")



