#
## 53. Count number of bits to be flipped to convert A to B ( A and B are two numbers given)
#

numberA = 32
numberB = 59
## TIP: {0:b} format method is faster than bin() to convert int => binary
print("Number {0} binary is: {1:b}".format( numberA, numberA))
print("Number {0} binary is: {1:b}".format( numberB, numberB))

print("Number %d binary is: %s" % ( numberA, bin(numberA)[2:]))
print("Number %d binary is: %s" % ( numberB, bin(numberB)[2:]))

## The longer - logical way
binaryA = ''
while numberA > 0:
    if numberA % 2 == 1:
        binaryA += '1'
    else:
        binaryA += '0'
    numberA //= 2
numberA = 32
numberB = 59
print( "Number",numberA,"in binary is:",binaryA)
print(numberA^numberB)
numberC = format(numberA^numberB,'08b')
print(numberC.count('1'), "bits needs to be flipped to convert {} to {}".format(numberA, numberB))

