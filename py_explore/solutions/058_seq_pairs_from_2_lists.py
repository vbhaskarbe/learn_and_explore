#
## 58. List1 = [ ‘a’, ‘b’, ‘c’, ‘d’] ; 
##     List2 = [ ‘p’, ‘q’, ‘r’, ’s’] 
#   Write a python program to print 
#    * ap
#    * bq
#    * cr
#    * ds
#
list1 = [ 'a', 'b', 'c', 'd']
list2 = [ 'p', 'q', 'r', 's']
for l1, l2 in zip( list1, list2):
    print("* {}{}".format(l1,l2))


