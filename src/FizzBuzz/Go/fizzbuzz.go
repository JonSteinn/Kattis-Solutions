package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scanf("%d %d %d", &a, &b, &c)

	for i:=1;i<=c;i++ {
		if i % a == 0 {
			if i % b == 0 {
				fmt.Println("FizzBuzz")
			} else {
				fmt.Println("Fizz")
			}
		} else if i % b == 0{
			fmt.Println("Buzz")
		} else {
			fmt.Println(i)
		}
	}
}