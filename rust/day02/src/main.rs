use std::io::{self, BufRead};

enum IntcodeOp {
    Add = 1,
    Mul = 2,
    Stop = 99,
}

#[derive(Debug)]
enum IntcodeError {
    InvalidOpcode,
}

fn run_intcode(code: &mut Vec<i32>) -> Result<i32, IntcodeError> {
    let mut i = 0;
    let mut target;
    let mut result;
    let mut op;
    loop {
        op = code[i];
        match op {
            op if op == IntcodeOp::Add as i32 => {
                target = code[i + 3] as usize;
                result = code[code[i + 1] as usize] + code[code[i + 2] as usize];
                code[target] = result;
                i += 4;
            }
            op if op == IntcodeOp::Mul as i32 => {
                target = code[i + 3] as usize;
                result = code[code[i + 1] as usize] * code[code[i + 2] as usize];
                code[target] = result;
                i += 4;
            }
            op if op == IntcodeOp::Stop as i32 => return Ok(code[0]),
            _ => return Err(IntcodeError::InvalidOpcode),
        }
    }
}

fn main() {
    let mut code: Vec<i32> = Vec::new();
    for line in io::stdin().lock().lines() {
        code = line
            .unwrap()
            .trim()
            .split(',')
            .map(|x| x.parse().unwrap())
            .collect();
    }
    let mut part1 = code.clone();
    let mut part2 = code.clone();
    part1[1] = 12;
    part1[2] = 2;
    let res1 = run_intcode(&mut part1).unwrap();
    println!("part1: {}", res1);

    'outer: for i in 0..100 {
        for j in 0..100 {
            part2[1] = i;
            part2[2] = j;
            let mut res2 = run_intcode(&mut part2).unwrap();
            if res2 == 19690720 {
                res2 = 100 * i + j;
                println!("part2: {}", res2);
                break 'outer;
            }
            part2 = code.clone();
        }
    }
}
