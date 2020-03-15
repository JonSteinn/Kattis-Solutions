def evaluate(var_vals, exp):
    var_stack, op_stack = ([],[])
    ops = {
        '*': lambda: var_stack.pop() and var_stack.pop(),
        '+': lambda: var_stack.pop() or var_stack.pop(),
        '-': lambda: not var_stack.pop()
    }

    for c in exp:
        if c in ops:
            op_stack.insert(0, c)
        else:
            var_stack.insert(0, var_vals[ord(c) - 65])

    while op_stack:
        var_stack.append(ops[op_stack.pop()]())

    return var_stack.pop()

def main():
    input() # dump
    var_vals=list(map(lambda z: True if z=='T' else False, input().split()))
    exp = input().split()
    print('T' if evaluate(var_vals, exp) else 'F')

if __name__ == "__main__":
    main()