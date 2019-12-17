#!/usr/bin/env python3

import fileinput

def part1(m):
    return m // 3 - 2

def part2(m):
    s = 0

    m = part1(m)
    while m > 0:
        s += m
        m = part1(m)

    return s

def main():

    d = [int(line) for line in fileinput.input()]
    total = sum(map(part1, d))
    total_fuel = sum(map(part2, d))

    print(f'part1: {total}')
    print(f'part2: {total_fuel}')

if __name__ == '__main__':
    main()
