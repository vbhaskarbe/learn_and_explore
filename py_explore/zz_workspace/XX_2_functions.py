
## dfunc_timer() - Decorator method; Time of execution of a function ##
import functools
import time
def dfunc_timer( function):
    @functools.wraps(function)
    def f_timer( *args, **kwargs):
        start_time = time.perf_counter()
        value      = function( *args, **kwargs)
        run_time   = time.perf_counter() - start_time
        print(f"Finished {function.__name__!r} function call in {run_time:.4f} secs")
        return value
    return f_timer

## factorial() - Method
def factorial( num):
    'A method to find factorial of a given number'
    return 1 if num == 1 else  num * factorial(num - 1)

## is_prime() - Method
def is_prime( number):
    for num in range(2, number // 2):
        if number % num == 0:
            return False
    return True

@dfunc_timer
def sum_of_numbers(n):
    total = 0
    for num in range(1, n+1):
        time.sleep(0.05)
        total = total + num
    return total

