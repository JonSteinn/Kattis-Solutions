package main

import (
	"fmt"
)
func main() {

	ball := 1
	var sequence string
	fmt.Scanln(&sequence)

	for _, char := range sequence {
		move(&ball, char)
	}

	fmt.Println(ball)
}

// Swap command
func move(ball *int, char int32) {
	if char == 65 {
		A(ball)
	} else if char == 66 {
		B(ball)
	} else {
		C(ball)
	}
}

// Swap cups 1 & 2
func A(ball *int) {
	if *ball == 1 {
		*ball = 2
	} else if *ball == 2 {
		*ball = 1
	}
}

// Swap cups 2 & 3
func B(ball *int) {
	if *ball == 2 {
		*ball = 3
	} else if *ball == 3 {
		*ball = 2
	}
}

// Swap cups 1 & 3
func C(ball *int) {
	if *ball == 1 {
		*ball = 3
	} else if *ball == 3 {
		*ball = 1
	}
}