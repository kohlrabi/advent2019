#!/usr/bin/env python3

import fileinput

from collections import UserDict


class Intcode(UserDict):
    
    
    def __register_opcodes(self):
        self.opcodes = {
            1: self.op_add,
            2: self.op_multiply,
            99: self.op_fini,
        }
    
    def __init__(self, regs={}):
        try:
            self.data = {k: v for k, v in regs.items()}
        except AttributeError:
            self.data = {i: reg for i, reg in enumerate(regs)}
        self.__register_opcodes()
                 
    def op_add(self):
        cur = self.cur
        self[self[cur+2]] = self[self[cur+0]] + self[self[cur+1]]
        return 3
    
    def op_multiply(self):
        cur = self.cur
        self[self[cur+2]] = self[self[cur+0]] * self[self[cur+1]]
        return 3
             
    def op_fini(self):
        raise StopIteration
        
    def run(self):
        self.cur = 0
        try:
            while True:
                opcode = self.opcodes[self[self.cur]]
                self.cur += 1 # opcode read, advance by 1
                self.cur += opcode() # run the operation
        except StopIteration:
            return
        
    def copy(self):
        return Intcode(self.data)

            
def part1(a: Intcode):
    a[1] = 12
    a[2] = 2
    
    a.run()
    
def part2(a: Intcode, magic: int=19690720):
    b = a.copy()
    for noun in range(100):
        for verb in range(100):
            a[1], a[2] = noun, verb
            a.run()
            if a[0] == magic:
                return 100 * noun + verb
            a = b.copy()

def main():
    regs = list(map(int, next(fileinput.input()).split(',')))
    
    a = Intcode(regs)
    b = a.copy()
    
    part1(a)
    print(f'part1: {a[0]}')
    r = part2(b)
    print(f'part2: {r}')
    
if __name__ == '__main__':
    main()    
    