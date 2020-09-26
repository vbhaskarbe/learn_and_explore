/* Print prime numbers upto 100 using nested loops */

package main

import (
	"fmt"
)

func main() {
	var ivar, jvar int
	for ivar = 2; ivar < 100; ivar++ {
		for jvar = 2; jvar <= (ivar / jvar); jvar++ {
			if (ivar % jvar == 0 ) {
				break;
			}
		}
		if ( jvar > (ivar / jvar)) {
			fmt.Printf("%d is Prime\n", ivar)
		}
	}
}


