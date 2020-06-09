from builtins import int, input
def fibonacci(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for _ in range(2, n):
            c= a+b
            a = b
            b = c
            print(c)
n = int(input("enter a number:- "))
fibonacci(n)
