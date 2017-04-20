package main

import (
	"fmt"
	"math"
)

func main() {
	var test_cases int
	fmt.Scanln(&test_cases)
	for i:=0;i<test_cases;i++ {
		var velocity, angle, x_position, h_min, h_max float64
		fmt.Scanf("%f %f %f %f %f\n", &velocity, &angle, &x_position, &h_min, &h_max)
		var y_position float64 = get_y_position(velocity, get_time(velocity, angle, x_position), angle)
		if h_min + 1 < y_position && y_position < h_max - 1 {
			fmt.Println("Safe")
		} else {
			fmt.Println("Not Safe")
		}
	}
}

// Algebra:

func get_time(velocity float64, angle float64, x_position float64) float64 {
	return x_position / (velocity * math.Cos(angle * math.Pi / 180.0))
}

func get_y_position(velocity float64, time float64, angle float64) float64 {
	return velocity * time * math.Sin(angle * math.Pi / 180.0) - 0.5 * 9.81 * time * time
}