#
## 57. Find the most frequent value in a given list
#

list_vals = [ 11, 12, 11, 18, 10, 9, 11, 78, 88, 63, 18, 11, 18, 19, 33, 18 ]
print("The list of values are: ", list_vals)
val_dict = {}
for lval in list_vals:
    if lval in val_dict.keys():
        val_dict[lval] += 1
    else:
        val_dict[lval] = 0
mfreq = max(val_dict.values())

for key in val_dict.keys():
    if mfreq == val_dict[key]:
        print("The number", key,"appears max",mfreq,"times in the list")



