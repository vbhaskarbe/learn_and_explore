

start = 120
end   = 180
print("Even numbers between {} and {} are: ".format(start, end))
for num in range(start, end):
    if num % 2 == 0:
        print(num, end=' ')
print()

print( [num for num in range(start, end) if num % 2 == 0])

gen_list = (num for num in range(start, end) if num % 2 == 0)
for gen_iter in gen_list:
    print( gen_iter, end=' ')
print()

def yeven():
    for num in range(start, end):
        if num % 2 == 0:
            yield num

for num in yeven():
    print( num, end=' ')
print()

def feven( num):
    if num % 2 == 0:
        return True 
            
print( list(filter( feven, range(start, end))))



