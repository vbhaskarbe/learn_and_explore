# to check whether a number is leap year or not

def leap_year_or_not(year):
    if(year%4==0 and year%100!=0 or year%400==0):
        print("it is a leap year: ")
    else:
        print("it is not a leap year:-")
        
year = int(input("Enter year to check:- "))      
leap_year_or_not(year)#function calling