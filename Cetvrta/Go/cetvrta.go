package main

import "fmt"

func main() {
	x_cnt := make(map[int]int)
	y_cnt := make(map[int]int)

	for i := 0; i < 3; i++ {
		var x, y int
		fmt.Scanf("%d %d", &x, &y)
		x_cnt[x]++
		y_cnt[y]++
	}

	for key,value := range x_cnt {
		if value == 1 {
			fmt.Printf("%d ", key)
			break
		}
	}

	for key,value := range y_cnt {
		if value == 1 {
			fmt.Println(key)
			break
		}
	}
}