#
## 19. Python program to Count occurrences of an element in a list
#

list1 = [ 50, 10, 30, 60, 40, 20, 90, 80, 70, 10, 10, 40 ]
list2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'a', 'x', 'a']

item1  = 100
item1a = 10
item2  = 'z'
item2a = 'a'

count1 = count2 = 0
for element in list1:
    if item1 == element:
        count1 += 1
    elif item1a == element:
        count2 += 1

print("Elements in list1 are: ", list1)
print("Element {} occurs {} times in list1".format( item1, count1))
print("Element {} occurs {} times in list1".format( item1a, count2))

count1 = count2 = 0
for element in list2:
    if item2 == element:
        count1 += 1
    elif item2a == element:
        count2 += 1

print("Elements in list2 are: ", list2)
print("Element {} occurs {} times in list2".format( item2, count1))
print("Element {} occurs {} times in list2".format( item2a, count2))

