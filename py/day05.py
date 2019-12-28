#!/usr/bin/env python3

import fileinput

from day02 import Intcode as Intcode2
from day02 import consume_iter

class Intcode(Intcode2):

    def __register_opcodes(self):
        super().__register_opcodes()

        self.__opcodes.update({
            1: self._op_add,
            2: self._op_mul,
            3: self._op_inp,
            4: self._op_outp,
            5: self._op_jnz,
            6: self._op_jez,
            7: self._op_slt,
            8: self._op_seq,
        })
        
    def __register_modes(self):
        self.__modes = {
            0: lambda i: self[self.cur+i],
            1: lambda i: self.cur+i,
        }

    def __init__(self, regs={}, input=0):
        super().__init__(regs)
        self.__register_modes()
        self.input = input
        self.output = []
        
    def _select_mode(self, modes):
        opers = []
        for i, mode in enumerate(modes):
            opers.append(self.__modes[mode](i))
        return opers

    def __next__(self):
        op = self[self.cur]
        opcode = op%100
        opcode = self.__opcodes[opcode]
        modes = []
        for i in range(2, 5):
            modes.append((op//(10**i))%10)
        self.cur += 1
        opers = self._select_mode(modes)
        shift = opcode(opers)
        self.cur += shift

    def run(self, input=0):
        self.input = input
        self.output = []
        consume_iter(self)
        return self.output

    def _op_add(self, opers):
        self[opers[2]] = self[opers[0]] + self[opers[1]]
        return 3

    def _op_mul(self, opers):
        self[opers[2]] = self[opers[0]] * self[opers[1]]
        return 3

    def _op_inp(self, opers):
        self[opers[0]] = self.input
        return 1

    def _op_outp(self, opers):
        self.output.append(self[opers[0]])
        return 1

    def _op_jnz(self, opers):
        if self[opers[0]] != 0:
            self.cur = self[opers[1]]
            return 0
        return 2

    def _op_jez(self, opers):
        if self[opers[0]] == 0:
            self.cur = self[opers[1]]
            return 0
        return 2
    
    def _op_slt(self, opers):
        self[opers[2]] = 1 if self[opers[0]] < self[opers[1]] else 0
        return 3
    
    def _op_seq(self, opers):
        self[opers[2]] = 1 if self[opers[0]] == self[opers[1]] else 0
        return 3
    
    def __call__(self, input=0):
        return self.run(input)
        

def main():
    regs = list(map(int, next(fileinput.input()).split(',')))

    a = Intcode(regs)
    b = a.copy()

    a = a(1)[-1]
    print(f'part1: {a}')
    b = b(5)[-1]
    print(f'part2: {b}')

if __name__ == '__main__':
    main()