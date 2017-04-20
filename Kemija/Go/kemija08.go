package main

import (
	"fmt"
	"bufio"
	"os"
)
func main() {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	input := scanner.Text()

	var skip int = 0
	for _,char := range input {
		if skip != 0 {
			skip--
		} else {
			fmt.Print(string(char))
			if isVowel(char) {
				skip = 2
			}
		}
	}
	fmt.Println()
}

func isVowel(c int32) bool {
	return c == 97 || c == 101 || c == 105 || c == 111 || c == 117
}