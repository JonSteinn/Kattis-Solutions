package main

import (
	"fmt"
)
func main() {
	cnt := [3]int{0, 0, 0} //TCG
	var input string
	fmt.Scanln(&input)
	for _,char := range input {
		if char == 84 { 			// T
			cnt[0]++
		} else if char == 67 { 		// C
			cnt[1]++
		} else { 					// G
			cnt[2]++
		}
	}
	// 7min(t,c,g)+t^2+c^2+g^2
	fmt.Println(
		7*min_int(cnt[0],min_int(cnt[1], cnt[2]))+cnt[0]*cnt[0]+
			cnt[1]*cnt[1]+ cnt[2]*cnt[2])
}
func min_int(x int, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}