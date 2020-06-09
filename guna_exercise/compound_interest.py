# compound interest
p = int(input("enter principal amount:- "))
t = int(input("enter time span:- "))
r = int(input("enter rate of interest:- "))
formula = p*(pow((1+(r/100)), t))
print(f'the compound interest is:- {formula}')