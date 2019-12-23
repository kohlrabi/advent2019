#!/usr/bin/env python3

minrange = 367479
maxrange = 893698

def digits(number):
    return [int(d) for d in str(number)]

def is_valid(number):
    digs = digits(number)
    two = 0
    for d, dd in zip(digs[0:], digs[1:]):
        if dd < d:
            return 0
        if d == dd:
            two = 1
    return two

def is_valid2(number):
    if not is_valid(number):
        return 0
    digs = digits(number)
    v = digs[0]
    l = 1
    for d in digs[1:]:
        if d == v:
            l += 1
        else:
            if l == 2:
                return 1
            v = d
            l = 1
    return l == 2

def part1():
    return sum(is_valid(n) for n in range(minrange, maxrange))

def part2():
    return sum(is_valid2(n) for n in range(minrange, maxrange))

def main():
    print('part1: {}'.format(part1()))
    print('part2: {}'.format(part2()))

if __name__ == '__main__':
    main()