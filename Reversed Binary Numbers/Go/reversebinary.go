package main

import (
	"fmt"
)
func main() {
	var old int
	var new int = 0
	fmt.Scanln(&old)
	for old != 0 {
		new = (new << 1) | (old & 0x1)
		old = old >> 1
	}
	fmt.Println(new)
}