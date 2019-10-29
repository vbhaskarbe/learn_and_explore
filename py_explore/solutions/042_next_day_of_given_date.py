#
## 42. Write a Python program to get next day of a given date.
#

from datetime import datetime, timedelta

print("Enter a date in format (dd/mm/yyyy):")
[ day, month, year ] = map(int, input().split('/'))
print("Next date for given date {}/{}/{} is {}".format(day, month, year, datetime(year, month, day) + timedelta(1)))

