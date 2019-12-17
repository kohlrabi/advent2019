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

total = 0
total_fuel = 0

for line in readlines()
    m = parse(Int, line)
    global total += part1(m)
    global total_fuel += part2(m)
end


using Printf

@printf("part1: %d\n", total)
@printf("part2: %d\n", total_fuel)
