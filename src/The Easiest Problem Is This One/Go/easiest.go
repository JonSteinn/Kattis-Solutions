package main

import (
	"fmt"
)

func main() {

	for ; ; {
		var number int
		fmt.Scanln(&number)

		if number==0 {
			break
		}
		ds := digit_sum(number)
		// A number is divisible by 3 <==> ds % 3 == 0 equiv A number is not divisible by 3 <==> ds%3!=0
		// There were more of these that are probably useful but im too lazy to look them up
		if ds % 3 != 0 {
			for i := 11;i<=100; i++ {
				if i%3==0 {
					continue
				}
				if digit_sum(i*number) == ds {
					fmt.Println(i)
					break
				}
			}
		} else {
			for i := 11;i<=100; i++ {
				if digit_sum(i*number) == ds {
					fmt.Println(i)
					break
				}
			}
		}

	}
}

func digit_sum(n int) int {
	sum := 0
	for n>9 {
		sum += n % 10
		n /= 10
	}
	return sum + n
}