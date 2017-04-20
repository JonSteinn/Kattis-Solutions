package main

import "fmt"

func main() {
	var h,m int
	fmt.Scanf("%d %d",&h,&m)
	m = ((m+60*h-45)+1440)%1440
	fmt.Printf("%d %d\n",m/60,m%60)
}