use std::io::{self, BufRead};

fn fuel(mass: i32) -> i32 {
    mass / 3 - 2
}

fn main() {
    let mut part1: i32 = 0;
    let mut part2: i32 = 0;

    for line in io::stdin().lock().lines() {
        let mut m: i32 = line.unwrap().trim().parse().unwrap();
        m = fuel(m);
        part1 += m;
        while m > 0 {
            part2 += m;
            m = fuel(m);
        }
    }
    println!("part 1: {}", part1);
    println!("part 2: {}", part2);
}
