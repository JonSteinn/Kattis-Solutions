package main

import (
	"fmt"
)

func main() {
	var a, b, c int
	fmt.Scanf("%d %d %d\n", &a, &b, &c)

	if a+b==c {
		fmt.Printf("%d+%d=%d\n",a,b,c)
	} else if a==b+c {
		fmt.Printf("%d=%d+%d\n",a,b,c)
	} else if a==b-c {
		fmt.Printf("%d=%d-%d\n",a,b,c)
	} else if a * b == c {
		fmt.Printf("%d*%d=%d\n",a,b,c)
	} else if a == b * c {
		fmt.Printf("%d=%d*%d\n",a,b,c)
	} else {
		fmt.Printf("%d=%d/%d\n",a,b,c)
	}
}