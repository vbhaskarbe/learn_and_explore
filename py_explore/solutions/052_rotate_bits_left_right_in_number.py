#
## 52. Rotate bits of a number/text (Left and Right)
#

number='1234567890'
rotate=3

print( number[len(number)-rotate:]+number[0:len(number)-rotate-1])


