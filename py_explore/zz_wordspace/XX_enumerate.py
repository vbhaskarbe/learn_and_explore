#
## Example usage for enumerate()
#

fruits = [ 'banana', 'apple', 'grape', 'pomogranate', 'berry', 'watermalon' ]

count = 1
for fruit in fruits:
    print("Fruit {} is {}".format(count, fruit))
    count = count + 1
print("*********************************************")

## WITH enumerate()
for count, fruit in enumerate(fruits):
    print("Indexing from 0: Fruit {} is {}".format(count, fruit))    
print("*********************************************")

for count, fruit in enumerate(fruits):
    print("Indexing from 1: Fruit {} is {}".format(count+1, fruit)) 
print("*********************************************")

## WITH enumerate() and start index
for count, fruit in enumerate(fruits, 1):
    print("Fruit {} is {}".format(count, fruit))    
print("*********************************************")


