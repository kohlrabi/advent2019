package main

import "fmt"

/* available opcodes */
const (
    OP_ADD = 1
    OP_MUL = 2
    OP_INP = 3
	OP_OUT = 4
	OP_JNZ = 5
	OP_JEZ = 6
	OP_SLT = 7
	OP_SEQ = 8
    OP_FIN = 99
)

func run_program(a map[int]int, input []int) int {
    var op, mode, output, oplen, inp int
    ops := [2]int{ 0, 0 }

    for i := 0; ; i += oplen {
        /* extract opcode */
		op = a[i] % 100
		/* extract mode flags
		 * 0: position mode
		 * 1: immediate mode
		 *
		 * we only need to extract the first two mode flags,
		 * the third parameter is always positional
		*/
        for j:=0; j<2; j++ {
            if(j == 0) {
                mode = (a[i] / 100) % 10
            } else {
                mode = (a[i] / 1000) % 10
            }
			if mode == 1 {
				ops[j] = a[i+j+1]
			} else {
				ops[j] = a[a[i+j+1]]
			}
		}

        switch op {
        case OP_ADD:
            a[a[i+3]] = ops[0] + ops[1]
            oplen = 4
        case OP_MUL:
            a[a[i+3]] = ops[0] * ops[1]
            oplen = 4
        case OP_INP:
            inp = input[0]
            input = input[1:]
            a[a[i+1]] = inp
            oplen = 2
        case OP_OUT:
            output = ops[0]
            oplen = 2
        case OP_JNZ:
            oplen = 3
            if ops[0] != 0 {
                i = ops[1]
                oplen = 0
            }
        case OP_JEZ:
            oplen = 3
            if ops[0] == 0 {
                i = ops[1]
                oplen = 0
            }
        case OP_SLT:
            if ops[0] < ops[1] {
                a[a[i+3]] = 1
            } else {
                a[a[i+3]] = 0
            }
            oplen = 4
        case OP_SEQ:
            if ops[0] == ops[1] {
                a[a[i+3]] = 1
            } else {
                a[a[i+3]] = 0
            }
            oplen = 4
        case OP_FIN:
            return output
        default:
            return -1
        }
    }
    return -1
}

// https://stackoverflow.com/a/30226442/1170207
func permutations(arr []int)[][]int{
    var helper func([]int, int)
    res := [][]int{}

    helper = func(arr []int, n int){
        if n == 1{
            tmp := make([]int, len(arr))
            copy(tmp, arr)
            res = append(res, tmp)
        } else {
            for i := 0; i < n; i++{
                helper(arr, n - 1)
                if n % 2 == 1{
                    tmp := arr[i]
                    arr[i] = arr[n - 1]
                    arr[n - 1] = tmp
                } else {
                    tmp := arr[0]
                    arr[0] = arr[n - 1]
                    arr[n - 1] = tmp
                }
            }
        }
    }
    helper(arr, len(arr))
    return res
}

func part1(a map[int]int) int {
    var prev int
    var b map[int]int
    var p[]int
    var inp[]int
    
    b = make(map[int]int)
    // store backup of a for pt 2
    for k, v := range a {
        b[k] = v
    }
    
    max := 0
    p = make([]int, 5)
    
    for i:=0; i<5; i++ {
        p[i] = i
    }

    for _, v := range permutations(p) {
        prev = 0
        for _, vv := range v {
            inp = []int{vv, prev}
            prev = run_program(a, inp)
            for k, v := range b {
                a[k] = v
            }
        }
        if prev > max {
            max = prev
        }
    }
    return max
}

//func part2(a map[int]int) int {
    //return run_program(a, 5)
//}

func main() {
    var m int
    var a,b map[int]int

    a = make(map[int]int)
    b = make(map[int]int)

    for i := 0; ; i++ {
        n, err := fmt.Scanf("%d", &m)
        if n == 0 || err != nil {
            break
        }
        a[i] = m
    }

    // store backup of a for pt 2
    for k, v := range a {
        b[k] = v
    }

    fmt.Printf("part1: %d\n", part1(a))
    //fmt.Printf("part2: %d\n", part2(b))
}
