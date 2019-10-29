#
## 43. Write a Python program to iterate over two lists simultaneously. 
#

days = ( 1, 2, 3, 4, 5, 6, 7 )
days_of_week = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
mapped = zip(days, days_of_week)
print( set(mapped))

for day, dow in zip( days, days_of_week):
    print( day,'=>', dow)

