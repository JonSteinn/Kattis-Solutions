package main

import (
	"fmt"
)
func main() {
	var stones int
	fmt.Scanln(&stones)
	if stones & 1 == 1 {
		fmt.Println("Alice")
	} else {
		fmt.Println("Bob")
	}
}