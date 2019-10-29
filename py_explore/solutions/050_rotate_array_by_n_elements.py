#
## 50. Python program to rotate an array by 'd' elements.
#

alist = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' ]
rotate_by = 3
print("The list of elements are       :", alist)
print("The list after rotating by {} is: {}".format( rotate_by, alist[len(alist) - rotate_by:len(alist):] + alist[0:len(alist) - rotate_by:]))

