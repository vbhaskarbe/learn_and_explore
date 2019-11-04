


# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
result = map(addition, numbers)
print(list(result))


numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

\
