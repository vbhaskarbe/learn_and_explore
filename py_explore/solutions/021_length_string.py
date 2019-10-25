#
## 21. Find length of a given string, first char, and last char in it
#

big_string = 'vegetables'
print("The string is                   :", big_string)
print("The length of the string is     :", len(big_string))
print("The first character in string is:", big_string[0])
print("The last character in string is :", big_string[-1])
print("The string reversed is          :", big_string[::-1])
print("The string in upper case is     :", big_string.upper())

vowels = [ 'a', 'e', 'i', 'o', 'u' ]
print("The vowels in the string are    :", set( [ char for char in big_string if char in vowels]))
print("The consonents in the string are:", set( [ char for char in big_string if char not in vowels]))


