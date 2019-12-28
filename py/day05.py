from day02 import Intcode as Intcode2

class Intcode(Intcode2):

    def __register_opcodes(self):
        super().__register_opcodes()

        self.opcodes.update({
            3: self.op_inp,
            4: self.op_outp,
            5: self.op_jnz,
            6: self.op_jez,
            7: self.op_slt;
            8: self.op_seq;
        })

    def __init__(self, regs={}, input=None):
        super().__init__(regs)
        self.input = input

    def __next__(self):
        op = self[self.cur]
        opcode = op%10
        opcode = self.opcodes[opcode]
        modes = ((op//100)%10, (op//1000)%10,)
        self.cur += 1
        opers = []
        for i, mode in enumerate(modes):
            if mode:
                opers.append(self.cur+i)
            else:
                opers.append(self[self.cur+i])
        self.cur += opcode(opers)

    def run(self, input=None):
        self.input = input
        for _ in self:
            pass
        return self.output

    def op_add(self, opers):
        self[self[cur+2]] = opers[0] + opers[1]
        return 3

    def op_multiply(self, opers):
        cur = self.cur
        self[self[cur+2]] = opers[0] * opers[1]
        return 3

    def op_inp(self, opers):
        cur = self.cur
        self[self[cur+1]] = self.input
        return 1

    def op_outp(self, opers):
        cur = self.cur
        self.output = self[cur]
        return 1

    def op_jez(self, opers):
        cur = self.cur
        if not opers[0]:
            self.cur = opers[1]
            return 0;
        return 2

    def op_jnz(self, opers):
        cur = self.cur
        if opers[0]:
            self.cur = opers[1]
            return 0;
        return 2
