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
    total = 0
    total_fuel = 0

    for line in fileinput.input():
        m = int(line)
        total += part1(m)
        total_fuel += part2(m)

    print(f'part1: {total}')
    print(f'part2: {total_fuel}')

if __name__ == '__main__':
    main()
