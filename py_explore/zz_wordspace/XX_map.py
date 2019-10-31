#
## map( function, iter)
#

list_orig = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

def add_numbers(num):
    return num + num

result = map( add_numbers, list_orig)
print("The new list is", list(result))

## Use lambda instead
list_orig1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
result     = map( lambda x: x + x, list_orig1)
print("The new list using lambda is", list(result))


## 
list_orig1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
list_orig2 = [ 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
result    = map( lambda one, two: one + two, list_orig1, list_orig2)
print("The new list is", list(result))


def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = list(map(lambda x: x(r), funcs))
    print(value)

