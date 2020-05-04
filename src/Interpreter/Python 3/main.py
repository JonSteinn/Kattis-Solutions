import sys

class Memory:
    RAM_SIZE = 1000
    REG_SIZE = 10
    MOD = 1000

    @staticmethod
    def create_from_input():
        mem = Memory()
        for i, line in enumerate(sys.stdin):
            mem.ram[i] = line[:-1]
        return mem

    def __init__(self):
        self.registers = [0] * Memory.REG_SIZE
        self.ram = ['000'] * Memory.RAM_SIZE
        self.ops = [
            self._op0,
            self._op1,
            self._op2,
            self._op3,
            self._op4,
            self._op5,
            self._op6,
            self._op7,
            self._op8,
            self._op9
        ]

    def exec(self):
        counter = 0
        i = 0
        while i < Memory.RAM_SIZE:
            counter += 1
            op,a,b = self.ram[i]
            i = self.ops[ord(op)-48](i, ord(a)-48, ord(b)-48)
        return counter

    def _op0(self, i, a, b):
        return i + 1 if self.registers[b] == 0 else self.registers[a]

    def _op1(self, i, a, b):
        return Memory.RAM_SIZE

    def _op2(self, i, a, b):
        self.registers[a] = b
        return i + 1

    def _op3(self, i, a, b):
        self.registers[a] = (self.registers[a] + b) % Memory.MOD
        return i + 1

    def _op4(self, i, a, b):
        self.registers[a] = (self.registers[a] * b) % Memory.MOD
        return i + 1

    def _op5(self, i, a, b):
        self.registers[a] = self.registers[b]
        return i + 1

    def _op6(self, i, a, b):
        self.registers[a] = (self.registers[a] + self.registers[b]) % Memory.MOD
        return i + 1

    def _op7(self, i, a, b):
        self.registers[a] = (self.registers[a] * self.registers[b]) % Memory.MOD
        return i + 1

    def _op8(self, i, a, b):
        self.registers[a] = int(self.ram[self.registers[b]])
        return i + 1

    def _op9(self, i, a, b):
        if self.registers[a] < 10:
            self.ram[self.registers[b]] = f'00{self.registers[a]}'
        elif self.registers[a] < 10:
            self.ram[self.registers[b]] = f'0{self.registers[a]}'
        else:
            self.ram[self.registers[b]] = str(self.registers[a])
        return i + 1

def main():
    print(Memory.create_from_input().exec())

if __name__ == "__main__":
    main()