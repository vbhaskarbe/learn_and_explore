/* A Go program showing function use as a closure */
package main
import "fmt"

func getSequence() func() int {
	i := 0
	return func() int {
		i = i + 1
		return i
	}
}

func main() {
	nextNum1 := getSequence()
	fmt.Println("Next number is:",nextNum1())
	fmt.Println("Next number is:",nextNum1())
	fmt.Println("Next number is:",nextNum1())
	fmt.Println("Next number is:",nextNum1())

	nextNum2 := getSequence()
	fmt.Println("New: Next number is :", nextNum2())
	fmt.Println("New: Next number is :", nextNum2())
	fmt.Println("New: Next number is :", nextNum2())
	fmt.Println("New: Next number is :", nextNum2())
	fmt.Println("New: Next number is :", nextNum2())

}

