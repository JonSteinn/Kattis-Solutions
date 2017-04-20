package main

import "fmt"

func main() {
	var n int;
	fmt.Scanln(&n)
	for i:=0;i<n;i++ {
		var next int;
		fmt.Scanln(&next)
		if next & 1 == 1 {
			fmt.Printf("%d is odd\n", next)
		} else {
			fmt.Printf("%d is even\n", next)
		}
	}
}