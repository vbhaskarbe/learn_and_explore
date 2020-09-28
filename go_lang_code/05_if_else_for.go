/* if..else and 'for' in code */
package  main

import "fmt"

func main() {
	var lower, upper int
	fmt.Printf("Enter lower limit ( 1 - 10)  : ")
	fmt.Scanf("%d", &lower)
	fmt.Printf("Enter upper limit ( 1 - 100) : ")
	fmt.Scanf("%d", &upper)

	fmt.Printf("You have entered: %d and %d\n", lower, upper)

	var counter int
	fmt.Printf("Numbers between %d and %d that are divisible by 5 are:\n", lower, upper)
	for counter = lower; counter <= upper; counter++ {
		if (counter % 5) == 0 {
			fmt.Printf("%d\n", counter)
		}
	}
}
