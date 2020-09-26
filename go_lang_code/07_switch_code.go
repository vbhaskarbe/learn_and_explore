/*
	A program showing use of 'switch' statement. Grades.
*/
package main

import "fmt"

func main() {
	/* Local variable declaration */
	var grade string  = "A"
	var avg_marks int = 80
	switch avg_marks {
		case 90: grade = "A"
		case 80,70: grade = "B"
		case 60,50: grade = "C"
		default : grade = "D"
	}

	switch {
		case grade == "A":
			fmt.Printf("Grade %s. Excellent.\n", grade)
		case grade == "B":
			fmt.Printf("Grade %s. Well Done.\n", grade)
		case grade == "C":
			fmt.Printf("Grade %s. You Passed.\n", grade)
		case grade == "D":
			fmt.Printf("Grade %s. Better try again.\n", grade)
		default :
			fmt.Printf("Grade %s. INVALID.", grade)
	}

}
