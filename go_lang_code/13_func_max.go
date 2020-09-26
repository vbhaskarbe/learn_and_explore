/* Go function max_num to find MAX of given 2 numbers */

package main

import "fmt"

func main() {
	var number1 int = 55
	var number2 int = 91
	var retValue int

	retValue = max_num(number1, number2)

	fmt.Printf("Max of numbers %d and %d is: %d", number1, number2, retValue)
	fmt.Println()
}

func max_num( num1, num2 int) int {
	var result int 
	if num1 > num2  {
		result = num1
	} else {
		result = num2
	}
	return result
}

