#
## 61. Python code to Swap keys with values in a dictionary? DICT comprehension
#

dict_week = {
                'One'   : 'Monday',
                'Two'   : 'Tuesday',
                'Three' : 'Wednesday',
                'Four'  : 'Thursday',
                'Five'  : 'Friday',
                'Six'   : 'Saturday',
                'Seven' : 'Sunday'
            }

print( "The dictiory before swap of keys with values:")
print( dict_week)

print( "The dictiory after swap")
## TIP: dict_variable = {key:value for (key,value) in dictonary.items()}
print( { v: k for k, v in dict_week.items()})

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
print(dict1_tripleCond)


