#
## filter()
#

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(list(filter(lambda x: x in a, b)))  # prints out [2, 3, 5, 7]

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print([x for x in a if x in b]) # prints out [2, 3, 5, 7]

