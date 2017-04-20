package main

import "fmt"

func main() {
	var input string
	fmt.Scanln(&input)

	cnt := 0
	cmp := [3]int32{80,69,82}
	for i,c := range input {
		if cmp[i%3] != c {
			cnt++;
		}
	}
	fmt.Println(cnt)
}