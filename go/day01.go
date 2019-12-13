package main

import "fmt"

func part1(m int) int {
    return m / 3 - 2
}

func part2(m int) int {
    sum := 0
    for {
        m = part1(m)
        if m <= 0 {
            break
        }
        sum += m
    }
    return sum
}

func main() {
    var m int

    total, total_fuel := 0, 0

    for {
        n, err := fmt.Scanf("%d\n", &m)
        if n == 0 || err != nil {
            break
        }
        total += part1(m)
        total_fuel += part2(m)
    }
	fmt.Printf("part1: %d\n", total)
	fmt.Printf("part2: %d\n", total_fuel)
}

