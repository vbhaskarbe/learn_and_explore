#
## Learning dictionaries and operations 
#

#import XX_1_data
#print( XX_1_data.__dict__)

from XX_1_data import d_charList, d_numList, d_daysOfWeek, d_monthsOfYear
import XX_2_functions as flib
from XX_2_functions import factorial as fact

if __name__ == '__main__':
    print( flib.__file__)
    print( d_charList)
    print( d_numList)
    print( d_daysOfWeek)
    print( d_monthsOfYear)

    print( flib.factorial(5))
    print( fact(5))
    print( "59 is prime? :", flib.is_prime(59))
    print( "128 is prime?:", flib.is_prime(128))
    print( "The sum of first 50 numbers is : ", flib.sum_of_numbers(10))


