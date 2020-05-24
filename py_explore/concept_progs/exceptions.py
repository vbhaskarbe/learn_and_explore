## Python exception handling ##

#import sys

try:
    a = 1
    b = 0
#    if b == 0:
#        raise ValueError
    result = a / b
    
except ValueError:
    print("ValueError exception seen")
except ZeroDivisionError:
    print("ZeroDivisionError exception seen")
except Exception as e:
    print("Exception seen: %s" % str(e))
#except:
#   print("Unexpected error:", sys.exc_info()[0])
#   raise
else:
    print("There was no exception")
finally:
    print("End of exception")


