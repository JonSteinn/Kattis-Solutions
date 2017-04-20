package main

import (
    "bufio"
    "os"
    "fmt"
)
func main() {
    var n, p int
    fmt.Scanf("%d", &n)
    fmt.Scanf("%d", &p)

    for i := 0; i < n; i++ {
        in := bufio.NewReader(os.Stdin)
        in.ReadString('\n')
    }

    fmt.Println(p)
}