/* Demonstrate subslicing */

package main

import "fmt"

func main() {
	numbers := []int{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
	printSlice( numbers)

	/* The original slice */
	fmt.Printf("Original slice :=> len = %d, cap = %d, and slice = %v\n", len( numbers), cap(numbers), numbers)

	/* Print the sub slice starting from index 1 (included) to index 4 (excluded) */
	fmt.Printf("numbers[1:4] = %v\n", numbers[1:4])

	/* Missing lower bound implies 0 */
	fmt.Printf("numbers[:3]  = %v\n", numbers[:5])

	/* 	Missing upper bound implies len(slice) */
	fmt.Printf("numbers[4:]  = %v\n", numbers[4:])

	numbers1 := make( []int, 0, 5)
	printSlice( numbers1)

	numbers2 := numbers[:2]
	printSlice( numbers2)

	numbers3 := numbers[2:5]
	printSlice( numbers3)
}

func printSlice( numlist []int) {
	fmt.Printf("printSlice: len = %d, cap = %d, and slice = %v\n", len( numlist), cap(numlist), numlist)
}

