package main

import "fmt"

func main() {
	var total_squares float64 = 0
	var cost float64
	var lawns int

	fmt.Scanln(&cost)
	fmt.Scanln(&lawns)

	for i:=0;i<lawns;i++ {
		var h, w float64
		fmt.Scanf("%f %f", &h, &w)
		total_squares += h * w
	}
	
	fmt.Println(total_squares * cost)
}