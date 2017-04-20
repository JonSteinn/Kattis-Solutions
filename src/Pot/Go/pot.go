package main

import (
"fmt"
)

func main() {
    var sum int = 0

    var n int;
    fmt.Scanln(&n);

    var next int
    for i:=0; i<n; i++ {
        fmt.Scanln(&next)
        sum += intPow(next / 10, next % 10)
    }

    fmt.Println(sum)
}

func intPow(a int, b int) int {
    var prod int = 1
    for ;b!=0; {
        if b&1!=0 { prod *= a }
        b >>= 1
        a *= a
    }
    return prod
}