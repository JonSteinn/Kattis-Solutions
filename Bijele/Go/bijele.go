package main

import (
	"fmt"
	"bytes"
	"strconv"
)
func main() {

	pieces := [6]int{1, 1, 2, 2, 2, 8} // K, Q, R, B, Kn, P
	var next int
	var buffer bytes.Buffer
	for i, v := range pieces {
		fmt.Scan(&next)
		buffer.WriteString(strconv.Itoa(v - next))
		if i == len(pieces)-1 {
			buffer.WriteString("\n")
		} else {
			buffer.WriteString(" ")
		}
	}
	fmt.Print(buffer.String())
}