#!/usr/bin/env python3

import fileinput
import sys

from collections import UserDict, deque
from typing import Iterable


def consume_iter(it: Iterable):
    """
    Helper function which fully consumes an iterator
    
    The idiomatic way to consume an iterator just for its side-effects in CPython 
    is to iterate it into a zero-length deque, this runs in a C-speed fast-path.
    
    When using PyPy (or other interpreters), prefer running a normal for-loop.
    
    See https://stackoverflow.com/a/50938015 and https://stackoverflow.com/a/50938287
    """
    if sys.implementation.name == 'cpython':
        deque(it, maxlen=0)
    else:
        for _ in it:
            pass


class Intcode(UserDict):
    """
    Intcode processor for day 2 of AoC 2019
    """
    
    def __getitem__(self, *args, **kwargs):
        try:
            return super().__getitem__(*args, **kwargs)
        except KeyError:
            return 0

    def __register_opcodes(self):
        """
        Register all opcodes of the Intcode processor
        
        An opcode has to return the number of registers the processing pointer has to advance,
        usually this will be the amount of operands consumed by the opcode.
        """
        self.__opcodes = {
            1: self._op_add,
            2: self._op_mul,
            99: self._op_halt,
        }

    def __init__(self, regs: Iterable={}):
        super().__init__()
        # we copy the input dict to ensure it is not changed
        try:
            # is this a dict?
            self.data = {k: v for k, v in regs.items()}
        except AttributeError:
            # Not a dict, but a list or tuple
            self.data = {i: reg for i, reg in enumerate(regs)}
        self.__register_opcodes()

    def _op_add(self, *args, **kwargs):
        """
        Add two operands, store the result in the third operand
        
        Advances the processing pointer by 3.
        """
        cur = self.cur
        self[self[cur+2]] = self[self[cur+0]] + self[self[cur+1]]
        return 3

    def _op_mul(self, *args, **kwargs):
        """
        Multiply two operands, store the result in the third operand
        
        Advances the processing pointer by 3.
        """
        cur = self.cur
        self[self[cur+2]] = self[self[cur+0]] * self[self[cur+1]]
        return 3

    def _op_halt(self, *args, **kwargs):
        """
        Halt the processor
        """
        raise StopIteration

    def __next__(self):
        """
        Processes the next opcode
        """
        opcode = self.__opcodes[self[self.cur]]
        self.cur += 1
        self.cur += opcode()

    def __iter__(self):
        """
        Entry point for the processor. It always starts at address 0
        """
        self.cur = 0
        return self

    def run(self):
        """
        Run the Intcode processor until it terminates with op_halt
        """
        consume_iter(self)

    def copy(self):
        """
        Create a deep-copy of an Intcode processor
        """
        return self.__class__(self.data)
    
    def __call__(self):
        self.run()


def part1(a: Intcode):
    a[1] = 12
    a[2] = 2

    a()

def part2(a: Intcode, magic: int=19690720):
    b = a.copy()
    for noun in range(100):
        for verb in range(100):
            a[1], a[2] = noun, verb
            a()
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
