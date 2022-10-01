import operator
import itertools

def expr(a, b, c, d):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}
    for op1, op2 in itertools.product(ops, ops):
        try:
            if ops[op1](a,b) == ops[op2](c,d):
                yield f"{a} {op1} {b} = {c} {op2} {d}"
        except ZeroDivisionError:
            pass


valid_expr = sorted(expr(*map(int, input().split())))
if valid_expr:
    print("\n".join(valid_expr))
else:
    print("problems ahead")