package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)
	for i:=0;i<n;i++ {
		var str1, str2 string
		fmt.Scanln(&str1)
		fmt.Println(str1)
		fmt.Scanln(&str2)
		fmt.Println(str2)
		for j:=0;j<len(str1);j++ {
			if str1[j]==str2[j] {
				fmt.Print(".")
			} else {
				fmt.Print("*")
			}
		}
		fmt.Println("\n")
	}
}