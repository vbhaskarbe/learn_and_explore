#
## 56. Using chaining of comparison operators find if a given number is between 90 and 200 ( 90 < n < 200 )
#

start = 90
end   = 200

number = int( input("Enter a number: "))

if ( start < number < end):
    print("The given number is between",start,"and",end)
else:
    print("The given number is NOT between",start,"and",end)

        
