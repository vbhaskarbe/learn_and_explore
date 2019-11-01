#
## filter()
#

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))  # prints out [2, 3, 5, 7]

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print([x for x in a if x in b]) # prints out [2, 3, 5, 7]

#Even number using filter function:
a = [1, 2, 3, 4, 5, 6]
filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

list_a = [1, 2, 3, 4, 5]
filter_obj = filter(lambda x: x % 2 == 0, list_a) # filter object <filter at 0x4e45890>
even_num = list(filter_obj) # Converts the filer obj to a list\
print(even_num) # Output: [2, 4]

