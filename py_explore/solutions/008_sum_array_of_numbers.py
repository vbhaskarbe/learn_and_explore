#
## 8. Sum of an array of numbers?
# 

print("Enter total number of array elements: ")
total = int( input())

my_list = []
for count in range(total):
    temp = int( input("Enter array element: "))
    my_list.append(temp)

sum_of_elements = 0
for element in my_list:
    sum_of_elements += element

print("The sum of elements ", my_list, 'is :', sum_of_elements)


