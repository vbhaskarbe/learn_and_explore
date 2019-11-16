
class Fibonacci_New( object):
    'This is a class for generating Fibonacci series'
    ## Constructor: Object being created.
    def __init__( self):
        self.values = [ 1, 1 ]

    def generate_series(self, upto_limit = 100 ):
        while self.values[ -1] < upto_limit:
            self.values.append( self.values[-1] + self.values[-2])

    def __str__(self):
        return("The fibonacci series is: {}".format(self.values))

    def __repr__(self):
        return("{}".format(self.values))

    ## Destructor : Object going out of scope
    def __del__(self):
        pass
        #print("Iam going to be destroyed")

    ## A Class method can be called directly with class, without creating an object of it.
    @classmethod
    def cm_message( cls):
        return('Iam the class method, which can be called even without an object')

if __name__ == '__main__':
    print("Executing as python script")
    print( Fibonacci_New.cm_message())
    fibo2 = Fibonacci_New()
    print( fibo2)
    print( fibo2.cm_message())
    fibo2.generate_series()
    print( fibo2)
    fibo2.generate_series(1000)
    print( fibo2)
    print( fibo2.__doc__)
    print( fibo2.__repr__())
    print( "------------------------------")
    fibo2_b = Fibonacci_New()    
    print( fibo2_b)
    print("*******************************")
    fibo2_c = Fibonacci_New()    
    print( fibo2_c.generate_series(50))
    print( fibo2_c)
    print( fibo2)
else:
    print("Importing.......")
    print("The name of the module is: ", __module__)
   
