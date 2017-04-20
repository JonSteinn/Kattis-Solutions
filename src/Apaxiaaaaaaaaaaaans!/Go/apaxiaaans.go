package main

import (
	"fmt"
)

func main() {
	var name string
	fmt.Scanln(&name)
	var last int32
	for _,c := range name {
		if c != last {
			fmt.Printf("%c", c)
			last = c
		}
	}
	fmt.Println()
}