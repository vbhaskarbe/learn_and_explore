#
## Sets in python
#

set1 = { 10, 90, 70, 30, 40, 10, 30, 80, 20, 40, 10 }
set2 = { 15, 25, 45, 35, 75, 65, 80, 10, 60 }
set3 = { 10, 30, 20 }
print( "The elements in the set1 are :", set1)
print( "Length of the set1 is        :", len(set1))
print( "The elements in the set2 are :", set2)
print( "Length of the set2 is        :", len(set2))
print( "The elements in the set3 are :", set3)
print( "Length of the set3 is        :", len(set3))

print( "Is 70 present in set1?       :", 70 in set1)
print( "Is 70 present in set1?       :", 70 not in set1)
print( "Is 85 present in set2?       :", 85 in set2)
print( "new Set with elements of both sets           :", set1.union( set2))
print( "new Set with elements common to both sets    :", set1.intersection( set2))
print( "new Set with elements in set1 but not in set2                :", set1.difference( set2))
print( "new Set with elements in either set1 or set2, but not in both:", set1.symmetric_difference( set2))
print( "Is every element in set1 is in set3?         :", set1.issubset( set3))
print( "Is every element in set3 is in set1?         :", set1.issuperset( set3))


