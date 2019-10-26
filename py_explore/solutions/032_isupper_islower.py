#
## 32. Check if given alphabet is in lower/upper case?
#

print("Enter an alphabet : ")
alphabet = input()

if alphabet.islower():
    print(alphabet, "is in lowercase")
    print(alphabet.upper(), "is the uppercase")
    print(ord(alphabet), "is the ASCII equivalent")
elif alphabet.isupper():
    print(alphabet, "is in uppercase")
    print(alphabet.lower(), "is the lowercase")
    print(ord(alphabet), "is the ASCII equivalent")

