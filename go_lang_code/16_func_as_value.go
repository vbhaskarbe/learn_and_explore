/* A Go function as value to variable */

package main

import "fmt"
import "math"

func main() {
	/* Declare a function variable */
	getSquareRoot := func( x float64) float64 {
		return math.Sqrt(x)
	}
	/* Use it */
	fmt.Println( getSquareRoot( 81))
}
