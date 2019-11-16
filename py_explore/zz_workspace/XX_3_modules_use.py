
#
## Learning dictionaries and operations 
#

#import XX_1_data
#print( XX_1_data.__dict__)

from XX_1_data import d_charList, d_numList, d_daysOfWeek, d_monthsOfYear
from XX_1_data import *
import XX_2_functions as flib
from XX_2_functions import factorial as imported_fact

if __name__ == '__main__':
    print( flib.__file__)
    print( "d_charList     :", d_charList)
    print( "d_numList      :",d_numList)
    print( "d_daysOfWeek   :",d_daysOfWeek)
    print( "d_monthsOfYear :",d_monthsOfYear)
    print( "d_text_word    :",d_text_word)
    print( "d_line_text    :",d_line_text)
    print( "d_range_start  :", d_range_start)
    print( "d_range_end    :", d_range_end)
    print( "d_int_number   :", d_int_number)
    print( "d_paragraph    :", d_paragraph)
    print()
    print( flib.factorial(5))
    print( imported_fact(5))
    print( "59 is prime? :", flib.is_prime(59))
    print( "128 is prime?:", flib.is_prime(128))
    print( "The sum of first 10 numbers is : ", flib.sum_of_numbers(10))


