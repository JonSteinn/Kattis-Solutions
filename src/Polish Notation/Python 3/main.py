import sys
from collections import deque

class Term:
    def __init__(self, s):
        self.value = None
        self.string = s
        if s.isnumeric() or s[1:].isnumeric():
            self.value = int(s)

    def is_number(self):
        return self.value is not None

    def __str__(self):
        return self.string

class Op:
    FUN = {'+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a,b: a*b}

    @staticmethod
    def is_op(s):
        return s in Op.FUN

    def __init__(self, s):
        self.op = s

    def eval(self, t1, t2):
        if t1.is_number() and t2.is_number():
            return Term(str(Op.FUN[self.op](t1.value,t2.value)))
        else:
            return Term(f'{self.op} {t1.string} {t2.string}')

def main():
    for case, line in enumerate(sys.stdin):
        val_stack, op_stack = deque(),deque()
        for x in reversed(line.split()):
            if Op.is_op(x):
                op_stack.append(Op(x))
            else:
                val_stack.append(Term(x))
            while len(op_stack) > 0 and len(val_stack) > 1:
                val_stack.append(op_stack.pop().eval(val_stack.pop(),val_stack.pop()))
        print(f'Case {case+1}: {val_stack.pop()}')

        
if __name__ == "__main__":
    main()