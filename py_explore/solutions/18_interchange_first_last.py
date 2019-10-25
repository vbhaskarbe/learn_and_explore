#
## 18. Python program to interchange first and last elements in a list
#

list_array     = [ 5, -1, 99, 101, 1, 10, 11, 54, 33 ]
print("The original list is                                       : ", list_array)
temp_store     = list_array[0]
list_array[0]  = list_array[-1]
list_array[-1] = temp_store
print("The new list after interchanging first <-> last element is : ", list_array)

