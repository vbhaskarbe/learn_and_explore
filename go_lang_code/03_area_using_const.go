/*	Find area using given Length and Width. Use const keyword 	*/
package main

import "fmt"

func main() {
	const LENGTH int = 45
	const WIDTH  int = 6 
	var area = LENGTH * WIDTH
	fmt.Printf("The area is = %d\n", area)
}

