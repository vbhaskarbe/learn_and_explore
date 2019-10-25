#
## 17. Python Program to find largest element in an array
#

list_array = [ 5, -1, 99, 101, 1, 10, 11, 54, 33 ]

smallest = largest = 0
for list_element in list_array:
    if smallest > list_element:
        smallest = list_element
    elif largest < list_element:
        largest = list_element

print("The array of unordered elements are : ", list_array)
print("The smallest element in the array is: ", smallest)
print("The largest element in the array is : ", largest)

## TIP: Unordered list can be sorted using sort() method
list_array.sort()
print("The array of ordered elements are          : ", list_array)
print("The smallest element in the sorted array is: ", list_array[0])
print("The largest element in the sorted array is : ", list_array[-1])


