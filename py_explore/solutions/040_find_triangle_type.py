#
## 
#

# Equilateral - All sides are of equal length
# Isosceles   - Two sides are of equal length
# Scalene     - All sides of different length


print( "Enter the length of 3 sides of a triangle:")
## TIP: More than one value can be read by using input() in list notation
tlengths = [ int(input()), int(input()), int(input()) ]
## TIP: Casting list_variable as set() will remove duplicates keeping only one copy
tlengths = set( tlengths)
if len( tlengths) == 1:
    print( "The triable is Equilateral since all sides are of equal length")
elif len( tlengths) == 2:
    print("The triangle is Isosceles since two of sides are of equal length")
else:
    print("The triangle is Scalene since all are the sides are of different lengths")

