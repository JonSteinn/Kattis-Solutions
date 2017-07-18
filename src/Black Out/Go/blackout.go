package main

import (
	"bufio"
	"os"
	"fmt"
	"strconv"
)

func main() {
	o := bufio.NewWriter(os.Stdout)

	var n int32
	fmt.Scan(&n)

	for ; n > 0; n--{
		o.WriteString("5 1 5 6\n")
		o.Flush()
		for ; ; {
			var cmd string
			fmt.Scan(&cmd)
			if cmd[0] != 'M' {
				break
			}
			var r1, c1, r2, c2 int
			fmt.Scan(&r1, &c1, &r2, &c2)
			if r2 == 5 {
				r2 = 4
			}
			o.WriteString(
				strconv.Itoa(5-r2) + " " + strconv.Itoa(7-c2) + " " +
					strconv.Itoa(5-r1) + " " + strconv.Itoa(7-c1) + "\n")
			o.Flush()
		}
	}

}
