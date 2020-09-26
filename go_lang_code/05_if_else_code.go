/*
	A program using 'if..else'
*/
package main

import "fmt"

func main() {
	var number int = 125
	//var number int = 25
	// if statement
	if ( number < 50 ) {
		fmt.Printf("number less than 50\n")
	} else {
		fmt.Printf("number is not less than 50\n")
	}
	fmt.Printf("value of number is : %d\n", number)

	// if..else if..else - Statement
	if ( number  == 30 ) {
		fmt.Printf("number is equal to 30\n")
	} else if ( number == 40 ) {
		fmt.Printf("number is equal to 40\n")
	} else if ( number == 50 ) {
		fmt.Printf("number is equal to 50\n")
	} else {
		fmt.Printf("None of the conditions match.\n")
	}

	// nested if
	var num1 int = 100
	var num2 int = 200
	if ( num1 == 100 ) {
		if ( num2 == 200 ) {
			fmt.Printf("num1 is 100 and num2 is 200\n")
		}
	}

}

