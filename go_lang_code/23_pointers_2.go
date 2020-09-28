/* Pointers with arrays in Go */
package main

import "fmt"

const MAX int = 3

func main() {
	inArray := []int{10, 100, 200}
	var lv int
	var aptr [MAX]*int;

	for lv = 0; lv < MAX; lv++ {
		aptr[lv] = &inArray[lv]
	}

	for lv = 0; lv < MAX; lv++ {
		fmt.Printf("Value of inArray[%d] = %d\n", lv, *aptr[lv])
	}
}
