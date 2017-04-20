package main

import "fmt"

func main() {
    for ;; {
        var n int
        fmt.Scanln(&n)
        if n==-1 {
            break
        }
        data_set(n)
    }
}

func data_set(count int) {
    var last_time, distance int = 0, 0
    for i:=0;i<count;i++ {
        var speed, time int
        fmt.Scanf("%d %d", &speed, &time)
        time -= last_time
        last_time += time
        distance += time * speed
    }
    fmt.Printf("%d miles\n", distance)
}