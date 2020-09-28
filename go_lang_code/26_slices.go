/* Example to show slices in Go language */

package main

import "fmt"

func main() {
	var numbers = make( []int, 3, 5)
	printSlice( numbers)
}

func printSlice( numlist []int) {
	fmt.Printf("len=%d, cap=%d, slice=%v\n", len( numlist), cap( numlist), numlist)
}
