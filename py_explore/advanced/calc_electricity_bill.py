
## Given an integer U denoting the amount of KWh units of electricity consumed, the 
## task is to calculate the electricity bill with the help of the below charges:
## 001 to 100    units - Rs.  6/unit
## 100 to 250    units - Rs.  8/unit
## 250 to 400    units - Rs. 12/unit
## 400 and above units - Rs. 15/unit

def calc_ebill( c_units):
    if c_units <= 100:
        return c_units * 6
    elif c_units <= 250:
        return ((100 * 6) + (c_units - 100) * 8)
    elif c_units <= 400:
        return ( (100 * 6) + (150 * 8) + ( c_units - 400) * 12)
    elif c_units > 400:
        return ( (100 * 6) + (150 * 8) + (150 * 12) + ( c_units - 600) * 15)

if __name__ == '__main__':
    print("Enter the number of units consumed: ")
    units_consumed = float( input())
    print("Your electricity bill amount is : ", calc_ebill( units_consumed))

