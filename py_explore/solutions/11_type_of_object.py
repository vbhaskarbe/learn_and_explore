#
## 11. Determine the type of an object in Python
#

list_obj = [ 
             12, 'Bhaskar', 3.0, ( 'a', 'b', 'c'), 
             { 'item1' : 'Onion', 'item2' : 'Tomato'}, 
             True, 2+5j, input, {"apple", "banana", "cherry"} 
           ]

for object_init in list_obj:
    print("Type of",str(object_init),"is", type(object_init))
print("Type of list_obj is", type(list_obj))


