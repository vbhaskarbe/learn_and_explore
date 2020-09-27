/* Go Arrays */

package main

import "fmt"

func main() {
	var emp_list [10] int
	var lv1, lv2 int
	for lv1 = 0; lv1 < 10; lv1++ {
		emp_list[lv1] = lv1 + 10
	}
	/* Print the array elements */
	for lv2 = 0; lv2 < 10; lv2++ {
		fmt.Printf("emp_list[%d] is: %d\n", lv2, emp_list[lv2])
	}
}
