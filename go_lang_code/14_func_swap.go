/* A Go function to swap 2 variables */
package main

import "fmt"

func main() {
	var name1 string = "Bhaskar"
	var name2 string = "Varadaraju"
	fmt.Printf("Before swapping: %s %s\n", name1, name2)
	name1, name2 = swap_vars( name1, name2)
	fmt.Printf(" After swapping: %s %s\n", name1, name2)
	fmt.Printf("Length of name1: %d\n", len( name1))
}

func swap_vars( text1, text2 string) (string, string) {
	return text2, text1
}

