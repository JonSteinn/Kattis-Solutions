package main

import (
	"fmt"
	"math"
)

func main() {
	for ;; {
		var radius float64
		var points, points_inside int
		fmt.Scanf("%f %d %d\n", &radius, &points, &points_inside)
		if radius == 0 {
			break
		}
		fmt.Printf("%f %f\n", radius*radius*math.Pi, 4.0*radius*radius*float64(points_inside)/float64(points))
	}
}