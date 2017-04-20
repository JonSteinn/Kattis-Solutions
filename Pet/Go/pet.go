package main

import (
	"fmt"
)
func main() {
	var best_row, best_score int = -1, -1

	for i:=1;i<6;i++ {
		var a, b, c, d int
		fmt.Scanf("%d %d %d %d", &a, &b, &c, &d)
		score:=a+b+c+d
		if (score > best_score) {
			best_row = i
			best_score = score
		}
	}
	fmt.Printf("%d %d\n", best_row, best_score)
}