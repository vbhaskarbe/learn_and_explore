/* A program to show call by reference in Go */

package main

import "fmt"

func main() {
	var num1, num2 int = 10, 20
	fmt.Printf("Before: Value of num1 is %d and num2 is %d\n", num1, num2)
	swap_orig( &num1, &num2)
	fmt.Printf("After : Value of num1 is %d and num2 is %d\n", num1, num2)
}

func swap_orig( item1 *int, item2 *int) {
	var temp int
	temp   = *item1
	*item1 = *item2
	*item2 = temp
}

