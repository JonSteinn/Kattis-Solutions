package main

import (
	"fmt"
)

var dominant_values = map[byte]int{
	'A' : 11,
	'K' : 4,
	'Q' : 3,
	'J' : 20,
	'T' : 10,
	'9' : 14,
	'8' : 0,
	'7' : 0,
}
var not_dominant_values = map[byte]int{
	'A' : 11,
	'K' : 4,
	'Q' : 3,
	'J' : 2,
	'T' : 10,
	'9' : 0,
	'8' : 0,
	'7' : 0,
}

func main() {
	var n int
	var dominant byte
	fmt.Scanf("%d %c\n", &n, &dominant)

	n <<= 2
	sum := 0
	for i:=0;i<n;i++ {
		sum += next_input(dominant)
	}

	fmt.Println(sum)

}

func next_input(dominant byte) int {
	var input string
	fmt.Scanln(&input)
	if input[1]==dominant {
		return dominant_values[input[0]]
	} else {
		return not_dominant_values[input[0]]
	}
}