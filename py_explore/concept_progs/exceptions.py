## Python exception handling ##
try:
    a = 1
    b = 0
#    if b == 0:
#        raise ValueError
    result = 1 / 0
    
except ValueError:
    print("ValueError exception seen")
except ZeroDivisionError:
    print("ZeroDivisionError exception seen")
except Exception as e:
    print("Exception seen: %s" % str(e))
else:
    print("There was no exception")
finally:
    print("End of exception")


