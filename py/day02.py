#!/usr/bin/env python3

import fileinput

from collections import UserDict


class Intcode(UserDict):
    """
    Intcode processor for day 2 of AoC 2019
    """
    
    def __register_opcodes(self):
        """
        Register all the opcodes of the Intcode processor
        """
        self.opcodes = {
            1: self.op_add,
            2: self.op_multiply,
            99: self.op_fini,
        }
    
    def __init__(self, regs={}):
        # we copy the input dict to ensure it is not changed
        try:
            # is this a dict?
            self.data = {k: v for k, v in regs.items()}
        except AttributeError:
            # Not a dict, but a list or tuple
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
    
    def __next__(self):
        opcode = self.opcodes[self[self.cur]]
        self.cur += 1
        self.cur += opcode()
        
    def __iter__(self):
        self.cur = 0
        return self
        
    def run(self):
        for _ in self:
            pass
        
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
    