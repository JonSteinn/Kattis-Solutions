package main

import (
	"fmt"
	"sync"
)

func main() {
	var min, max, val int
	fmt.Scanln(&min)
	fmt.Scanln(&max)
	fmt.Scanln(&val)

	var wg sync.WaitGroup
	wg.Add(2)

	// Find min
	go func() {
		defer wg.Done()
		for i:=min;i<=max;i++ {
			if digit_sum(i) == val {
				min = i
				break
			}
		}
	}()

	// Find max
	go func() {
		defer wg.Done()
		for i:=max;i>=min;i-- {
			if digit_sum(i) == val {
				max = i
				break
			}
		}

	}()

	wg.Wait()

	fmt.Println(min)
	fmt.Println(max)
}

func digit_sum(n int) int {
	sum := 0
	for ;n>0; {
		sum += n % 10
		n /= 10
	}
	return sum
}