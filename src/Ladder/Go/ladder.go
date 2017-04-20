package main

import (
	"fmt"
	"math"
)
func main() {
	var height, angle float64
	fmt.Scanf("%f %f", &height, &angle)
	fmt.Println(math.Ceil(height / math.Sin(math.Pi * angle / 180.0)))
}