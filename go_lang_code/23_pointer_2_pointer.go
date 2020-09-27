/* Go - Pointer to a pointer */

package main

import "fmt"

func main() {
	var first int
	var firstptr *int
	var secondptr **int

	first = 3000

	firstptr = &first

	secondptr = &firstptr

	fmt.Printf("The value of first = %d\n", first)
	fmt.Printf("The value of *firstptr = %d\n", *firstptr)
	fmt.Printf("The value of **secondptr = %d\n", **secondptr)

}
