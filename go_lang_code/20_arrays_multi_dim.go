/* Go program to show using Multi Dimensional arrays */
package main

import "fmt"

func main() {
	/* an array with 5 rows and 2 columns */
	var ma = [5][2] int { {0,0}, {1,2}, {2,4}, {3,6}, {4,8}}
	var row, col int
	for row = 0; row < 5; row++ {
		for col = 0; col < 2; col++ {
			fmt.Printf("ma[%d][%d] = %d\n",row, col, ma[row][col])
		}
	}
}
