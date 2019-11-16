#
## 44. Write a Python program to create a Caesar encryption.
#

## Encryption  => e(x) = (x + k) (mod 26)
## Descryption => e(x) = (x - k) (mod 26)

plain_text  = 'Lets meet At the dawn to plan the attack on enemy'
cipher_text = str()
cipher_key  = 5
print("Plain text is :", plain_text)

## ASCII value of 'A' is 65
## ASCII value of 'a' is 97
## Number of alphabets in english - 26
for char in plain_text:
    if char.islower():
        cipher_text += chr( (ord(char) + cipher_key - 97) % 26 + 97)
    elif char.isupper():
        cipher_text += chr( (ord(char) + cipher_key - 65) % 26 + 65)
    else:
        cipher_text += char

print("Cipher text is:", cipher_text)


