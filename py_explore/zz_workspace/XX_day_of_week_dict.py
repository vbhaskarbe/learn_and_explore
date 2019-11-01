
week_days = {
                1 : 'Monday',
                2 : 'Tuesday',
                3 : 'Wednesday',
                4 : 'Thursday',
                5 : 'Friday',
                6 : 'Saturday',
                7 : 'Sunday'
            }
print("Enter a number between 1-7:")
day = int( input())
if day < 1 or day > 7:
    print("The number is not in the range of 1-7")
else:
    print("Day {} of the week is {}".format( day, week_days[day]))


