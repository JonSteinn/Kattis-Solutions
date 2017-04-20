package main

import (
	"fmt"
)
func main() {
	set := make(map[int]bool)
	for i:=0;i<10;i++ {
		var next int
		fmt.Scanln(&next)
		set[next%42] = true
	}
	fmt.Println(len(set))
}