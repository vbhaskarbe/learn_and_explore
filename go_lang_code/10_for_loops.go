/*  Demonstrate different types of 'for' loops in Go */

package main

import "fmt"

func main() {
	var limit int = 15
	var start int
	numbers := [6] int {1, 2, 3, 5}

	// for type 1
	fmt.Println("for Type1")
	for start := 0; start < 10; start++ {
		fmt.Printf("Value of start is: %d\n", start)
	}

	// for type 2
	fmt.Println("for Type2")
	for start < limit {
		start++
		fmt.Printf("Value of start is: %d\n", start)
	}

	// for type 3
	fmt.Println("for Type3")
	for lv, x:= range numbers {
		fmt.Printf("Value of x is: %d at %d\n", x, lv)
	}
}
