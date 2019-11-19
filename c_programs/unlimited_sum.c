#include<stdio.h>
#include<stdarg.h> /* variable arg header */ 

/* A variable argument function that uses a for loop to get each argument
into a calculation. */
long addup(long a, ...)
{
  va_list args;  /* variable argument list */
  long sum = 0;
  long current = a;
  va_start(args, a); /* first arg (long)*/

  for( ; current; current = va_arg(args, int))
  { 
    sum = sum + current; 
  }
  va_end(args);  /* done getting args -- cleanup*/
  return sum;
}

/* fix because last arg has to be 0 */
#define addup(...)  addup( __VA_ARGS__ ,0);

int main()
{
  long x = addup( 5 ,4 ,6 ,7, -10, 333, 14, 11, 44);
  printf("Sum = %ld\n", x);
}
