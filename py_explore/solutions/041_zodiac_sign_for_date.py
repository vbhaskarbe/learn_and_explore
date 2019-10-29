#
## 41. Write a Python program to display English zodiac sign for given date of birth
#

from datetime import datetime

print("Enter your date of birth [ dd/mm ]: ")
[ day, month ] = [ int(x) for x in input().split('/') ] 
#print( day, month)

if ( ((month == 3) and (day >= 21)) or ((month == 4) and (day <= 19))):
    print("Your Zodiac sign is Aries")
if ( ((month == 4) and (day >= 20)) or ((month == 5) and (day <= 20))):
    print("Your Zodiac sign is Taurus")
if ( ((month == 5) and (day >= 21)) or ((month == 6) and (day <= 20))):
    print("Your Zodiac sign is Gemini")
if ( ((month == 6) and (day >= 21)) or ((month == 7) and (day <= 22))): 
    print("Your Zodiac sign is Cancer")
if ( ((month == 7) and (day >= 23)) or ((month == 8) and (day <= 22))):
    print("Your Zodiac sign is Leo")
if ( ((month == 8) and (day >= 23)) or ((month == 9) and (day <= 22))):
    print("Your Zodiac sign is Virgo")
if ( ((month == 9) and (day >= 23)) or ((month == 10) and (day <= 22))):
    print("Your Zodiac sign is Libra")
if ( ((month == 10) and (day >= 23)) or ((month == 11) and (day <= 21))):
    print("Your Zodiac sign is Scorpio")
if ( ((month == 11) and (day >= 22)) or ((month == 12) and (day <= 21))):
    print("Your Zodiac sign is Sagittarius")
if ( ((month == 12) and (day >= 22)) or ((month == 1) and (day <= 19))):
    print("Your Zodiac sign is Capricorn")
if ( ((month == 1) and (day >= 20)) or ((month == 2) and (day <= 18))):
    print("Your Zodiac sign is Aquarius")
if ( ((month == 2) and (day >= 19)) or ((month == 3) and (day <= 20))):
    print("Your Zodiac sign is Pisces")


zodiac = { 
            '21-03:19-04' : 'Aries',
            '20-04:20-05' : 'Taurus',
            '21-05:20-06' : 'Gemini',
            '21-06:22-07' : 'Cancer',
            '23-07:22-08' : 'Leo',
            '23-08:22-09' : 'Virgo',
            '23-09:22-10' : 'Libra',
            '23-10:21-11' : 'Scorpio',
            '22-11:21-12' : 'Sagittarius',
            '22-12:19-01' : 'Capricorn',
            '20-01:18-02' : 'Aquarius',
            '19-02:20-03' : 'Pisces'
         }
 


