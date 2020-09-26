/* A program to show use of break, continue, and goto 'loop control' statements */
package main
import "fmt"
func main() {
	var limit int = 10
	
	// Use of break
	for limit < 20 {
		fmt.Printf("Value of limit: %d\n", limit)
		limit++
		if limit > 15 {
			break;
		}
	}

	// Use of continue
	limit = 10
	for limit < 20 {
		if limit == 15 {
			limit = limit + 1
			continue
		}
		fmt.Printf("Value of limit - 2: %d\n", limit)
		limit++
	}

	// Use of goto
	limit = 10
	LOOP : for limit < 20 {
				if limit == 15 {
					limit += 1
					goto LOOP
				}
				fmt.Printf("Value of limitt - 3: %d\n", limit)
				limit++
			}
}
