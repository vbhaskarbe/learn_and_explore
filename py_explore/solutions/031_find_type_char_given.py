#
## 31. Find if give character is alphabet, Digit or special character?
#

while True:
    char = input("Enter any character ('z' to exit): ")
    if char == 'z':
        exit(1)
    if char.isalpha():
        print(char, "is Alphanumeric")
    elif char.isdigit():
        print(char, "is Digit")
    elif char.isspace():
        print(char, "is a Space")
    elif char.isprintable():
        print( char, "is Printable")
    else:
        print( char, "is UNKNOWN type")

        
