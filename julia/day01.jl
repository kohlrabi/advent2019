#!/usr/bin/env julia

function part1(m)::Int
    m ÷ 3 - 2
end

function part2(m)::Int
    s = 0

    m = part1(m)
    while m > 0
        s += m
        m = part1(m)
    end

    return s
end

d = [parse(Int, x) for x in readlines()]

total = sum(part1, d)
total_fuel = sum(part2, d)


using Printf
@printf("part1: %d\n", total)
@printf("part2: %d\n", total_fuel)
