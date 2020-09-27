/*
 a simple hello world program
*/
package main

import (
	"fmt"
	"time"
	"math/rand"
)

func main() {
	/* This is my first program */
	fmt.Println("Hello, World!")
	fmt.Println("Iam in Go Programming World!")
	fmt.Println("Time now is : ", time.Now())
	fmt.Println("Random number between 1 - 10 is: ", rand.Intn(10))
	fmt.Println("Random number between 1 - 10 is: ", rand.Intn(10))
	fmt.Println("Random number between 1 - 10 is: ", rand.Intn(10))

	var name string
	fmt.Printf("Enter your name: ")
	fmt.Scanf("%s", &name)
	fmt.Println("Hello,", name)
}

