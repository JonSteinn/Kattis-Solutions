package main

import (
"fmt"
)
func main() {
	var n, m int
	fmt.Scanln(&n, &m)
	min_max(&n, &m)
	for i:=n+1;i<m+2;i++ {
		fmt.Println(i)
	}
}

// If n>m then swap
func min_max(n *int, m *int) {
	if *n > *m {
		*n = *n ^ *m
		*m = *m ^ *n
		*n = *n ^ *m
	}
}