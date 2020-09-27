/* Demonstrate pointers in Go */
package main
import "fmt"

func main() {
	var value int = 20
	var vptr *int

	vptr = &value
	fmt.Printf("Address of 'value' variable is       : %x\n", &value)
	fmt.Printf("Address stored in 'vptr' variable is : %x\n", vptr)
	fmt.Printf("Value of '*vptr' variable is         : %d\n", *vptr)

	/* Value of uninitialized variable is 'nil' */
	var ptr *int
	fmt.Printf("Value stored in unintialized variable is : %x\n", ptr)
}
