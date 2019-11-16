

class Fibonacci( object):
    def __init__(self):
        self.values = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.values) > 1:
            self.values.append( self.values[-1] + self.values[-2])
        else:
            self.values.append(1)
        return self.values[-1]

if __name__ == '__main__':
    fib_div = 16
    for fib in Fibonacci():
        if fib % fib_div == 0:
            print("The first fibonacci number divisible by {} is: {}".format( fib_div, fib))
            break
        if fib > 10000:
            break

    print( Fibonacci())
