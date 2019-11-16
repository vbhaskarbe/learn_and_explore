
my_list1 = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
my_list2 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

print("Print a list along with index: Additional count variable")
count = 1
for day in (my_list1):
    print(count, "-->", day)
    count = count + 1
print('!' * 40)

print("Print a list along with index: enumerate( list)")
for dnum, day in enumerate( my_list1):
    print( dnum, '=>', day)
print('!' * 40)

print("Print a list along with index: enumerate( list, start = 0)")
for dnum, day in enumerate( my_list1, start = 1):
    print( dnum, '=>', day)
print('!' * 40)

print("Print a list along with index: enumerate( list, start = 100)")
for dnum, day in enumerate( my_list1, 100):
    print( dnum, '=>', day)
print('!' * 40)


