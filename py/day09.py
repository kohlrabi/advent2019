#!/usr/bin/env python3

import fileinput

from day05 import Intcode as Intcode5


class Intcode(Intcode5):
    
    def __init__(self, *args, **kwargs):
        self.relbase = 0
        super().__init__(*args, **kwargs)
    
    def __register_modes(self):
        super().__register_modes()
        self.__modes.update({
            2: lambda i: self[self[self.cur+i]+self.relbase]
        })
        
    def __register_opcodes(self):
        super().__register_opcodes()
        self.__opcodes.update({
            9: self._op_relbase
        })
        
    def _op_relbase(self, opers):
        self.relbase = opers[0]
        return 1


def main():
    regs = list(map(int, next(fileinput.input()).split(',')))

    a = Intcode(regs)
    b = a.copy()

    a = a(1)
    print(f'part1: {a}')
    #b = b(5)
    #print(f'part2: {b}')

if __name__ == '__main__':
    main()