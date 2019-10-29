#
## 45. Write a Python program to count repeated characters in a string . Sample string: 'thequickbrownfoxjumpsoverthelazydog’. 
#   Expected output :
#       o 4
#       e 3
#       u 2
#       h 2
#       r 2
#       t 2
#

text = 'thequickbrownfoxjumpsoverthelazydog'
print("The text is :", text)
letters_count = ([(x, text.count(x)) for x in text if text.count(x) > 1])
print("The duplicate letters in the text and their count is:")
for lc in letters_count:
    print(lc)

