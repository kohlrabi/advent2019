package main

import "fmt"

func part1(a [][][]int) int {
	var layer int

	z := make([]int, len(a))

	for i, aa := range a {
		zeros := 0
		for _, bb := range aa {
			for _, cc := range bb {
				if cc == 0 {
					zeros++
				}
			}
		}
		z[i] = zeros
	}

	min := 25 * 6
	layer = -1
	for i, v := range z {
		if v < min {
			min = v
			layer = i
		}
	}

	ones, twos := 0, 0
	for _, aa := range a[layer] {
		for _, bb := range aa {
			if bb == 1 {
				ones++
			} else if bb == 2 {
				twos++
			}
		}
	}

	return ones * twos
}

func readImageData() [][][]int {
	var c int
	var fin bool

	const width = 25
	const height = 6

	a := make([][][]int, 1)

	fin = false
	for i := 0; !fin; i++ {
		a[i] = make([][]int, height)
		for j := 0; j < height; j++ {
			a[i][j] = make([]int, width)
			for k := 0; k < width; k++ {
				n, err := fmt.Scanf("%1d", &c)
				if n == 0 || err != nil {
					fin = true
					break
				}
				a[i][j][k] = c
			}
		}
		if !fin {
			a = append(a, make([][]int, 1))
		}
	}
	return a
}

func main() {
	a := readImageData()

	fmt.Printf("part1: %d\n", part1(a))
}
