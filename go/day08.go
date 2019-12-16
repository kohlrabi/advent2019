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

func part2(a [][][]int) {

	height := len(a[0])
	width := len(a[0][0])

	image := make([][]int, height)

	for i := range image {
		image[i] = make([]int, width)
	}

	for i, v := range image {
		for j := range v {
			image[i][j] = 2
		}
	}

	for _, v := range a {
		for j, w := range v {
			for k, x := range w {
				if image[j][k] == 2 {
					image[j][k] = x
				}
			}
		}
	}

	for _, v := range image {
		for _, w := range v {
			if w == 0 {
				fmt.Printf(" ")
			} else {
				fmt.Printf("*")
			}
		}
		fmt.Printf("\n")
	}

}

func readImageData(height int, width int) [][][]int {
	var c int
	var fin bool

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
	const height = 6
	const width = 25

	a := readImageData(height, width)

	fmt.Printf("part1: %d\n", part1(a))
	fmt.Printf("part2:\n")
	part2(a)
}
