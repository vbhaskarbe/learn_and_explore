#
## 14. a way to remove the last object from a list?
#

list_of_items = [ 'item1', 'second', 'third', 'fourth', 'lastone' ]

## TIP: pop() to remove last item from list
## TIP: append() to add a new item at the end of list
print("The list is                         : ", list_of_items)
print("The last item from list is          : ", list_of_items.pop())
print("The list after removing last item is: ", list_of_items)
print("The item to be added to list is     : 'newlastitem'")
list_of_items.append('newlastitem')
print("The list after adding the last item : ", list_of_items)


