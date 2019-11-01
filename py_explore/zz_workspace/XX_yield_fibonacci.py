
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

gen = fibonacci()
for i, f in enumerate(gen):
    print(i, f)
    if i >= 10: break


