
lis_elements = [12, 12, 100, 90, 82, 190, 281, 172, 8, 9, 9, 8, 90, 90]
unique = []
for i in lis_elements:
    if i not in unique:
        unique.append(i) 
    
unique.sort()
print(unique)

