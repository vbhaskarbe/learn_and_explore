# Count number of bits to be flipped 
# to convert A into B 
  
# Function that count set bits 
def countSetBits( n ): 
    count = 0
    while n: 
        count += n & 1
        n >>= 1
    return count 
      
# Function that return count of 
# flipped number 
def FlippedCount(a , b): 
  
    # Return count of set bits in 
    # a XOR b 
    return countSetBits(a^b) 
  
# Driver code 
a = 32
b = 59
print(FlippedCount(a, b)) 
