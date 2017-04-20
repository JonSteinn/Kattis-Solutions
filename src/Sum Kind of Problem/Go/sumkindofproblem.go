package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanln(&n)

	for i:=0;i<n;i++ {
		var K, N int
		fmt.Scanf("%d %d\n", &K, &N)
		sq := N * N
		fmt.Printf("%d %d %d %d\n", K, (sq+N)>>1, sq, sq+N)
	}
}

// 1+2+...+n = n(n+1)/2 = (n^2+n)/2
// 1+3+...+2n-1 = ((2-1) + (4-1) + ... + (2n-1)) = (2+4+...2n)-n = 2(1+2+...+n)-n = 2n(n+1)/2-n = n^2
// 2+4+...+2n = 2(1+2+...+n) = 2n(n+1)/2 = n(n+1) = n^2+n