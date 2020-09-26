/* 
	Program to print float variable and type
*/
package main

import "fmt"

func main() {

	var f_var float64
	var number, name = 18, "Bhaskar"
	sum := number
	f_var = 20.0
	fmt.Println(f_var)
	fmt.Printf("The type of variable 'f_var' is %T and it has value %f\n", f_var, f_var)
	fmt.Printf("type of 'sum' by inference is %T\n", sum)
	fmt.Printf("type of 'name' is %T with value %s\n", name, name)
}

