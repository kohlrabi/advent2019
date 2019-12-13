package main

import "fmt"

const (
    OP_ADD = 1
    OP_MUL = 2
    OP_FIN = 99
)

func run_program(a []int) int {
    const oplen = 4

    for i := 0; ; i += oplen {
        switch a[i] {
        case OP_ADD:
            a[a[i+3]] = a[a[i+1]] + a[a[i+2]]
        case OP_MUL:
            a[a[i+3]] = a[a[i+1]] * a[a[i+2]]
        case OP_FIN:
            return 0
        default:
            return -1
        }
    }
    return -1
}

func part1(a []int) int {
    a[1] = 12
    a[2] = 2

    run_program(a)
    return a[0]
}

func part2(a []int) int {
    const magic = 19690720

    b := make([]int, len(a))
    copy(b, a)
    for noun := 0; noun < 100; noun++ {
        for verb := 0; verb < 100; verb++ {
            a[1], a[2] = noun, verb
            run_program(a)
            if a[0] == magic {
                return 100 * noun + verb
            }
            copy(a, b)
        }
    }
    return -1
}

func main() {
    var m int
    var a []int

    for {
        n, err := fmt.Scanf("%d,", &m)
        if n == 0 || err != nil {
            break
        }
        a = append(a, m)
    }
    // store backup of a for pt 2
    b := make([]int, len(a))
    copy(b, a)

    fmt.Printf("part1: %d\n", part1(a))
    fmt.Printf("part2: %d\n", part2(b))
}
