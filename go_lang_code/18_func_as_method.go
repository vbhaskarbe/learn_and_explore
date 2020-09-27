/* Function as method */
package main

import  (
	"fmt"
	"math"
)

type Circle struct {
	x, y, radius  float64
}

func ( circle Circle) area() float64 {
	return math.Pi * circle.radius * circle.radius
}

func main() {
	circle := Circle{ x:0, y:0, radius:5}
	fmt.Printf("Area of the circle is: %f\n", circle.area())
}

