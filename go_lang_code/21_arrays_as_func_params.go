/* Example to show arrays as function params */

package main

import "fmt"

func main() {
	/* an int array with 5 elements */
	var balance = [] int {	100, 2, 3, 17, 50 }
	var average float32

	/* pass array as an argument */
	average = getAverage( balance, len( balance))

	fmt.Println("Average value is:", average)
}

func getAverage(ba []int, size int) float32{
	var lv, sum int
	var avg float32

	for lv = 0; lv < size; lv++ {
		sum = sum + ba[lv]
	}

	avg = float32( sum / size)
	return avg
}
