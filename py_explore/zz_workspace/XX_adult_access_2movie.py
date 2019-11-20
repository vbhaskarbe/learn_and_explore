#
## Read in the current age
#
age = int(input("What's your age?"))

if age >= 18:
    print("Adult. Access allowed")
elif age < 18 and age > 0:
    print("Youngster. Access not allowed")
else:
    print("Error. Invalid age")
