
class Numbers( object):
    def __init__(self, n = 10):
        self.num = n

    def evenodd(self):
        if self.num % 2 == 0:
            return 'Even'
        else:
            return 'Odd'

if __name__ == '__main__':
    no = Numbers(199)
    print( no.evenodd())
    no = Numbers(18)
    print( no.evenodd())



