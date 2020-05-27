from collections import deque, Counter

class Evaluator:
    VARS = {'p', 'q', 'r', 's', 't'}
    OP = {
        'K': (2, lambda a,b: a and b),
        'A': (2, lambda a,b: a or b),
        'N': (1, lambda a: not a),
        'C': (2, lambda a,b: not a or b),
        'E': (2, lambda a,b: a==b),
    }
    SUCCESS = 'tautology'
    FAILURE = 'not'

    @staticmethod
    def get_vars_from_expression(expression):
        c = Counter(expression)
        v = [var for var in Evaluator.VARS if c[var] > 0]
        return v

    @staticmethod
    def _binary_strings_of_length(collect, lis, i, n):
        if i == n:
            collect.append(lis.copy())
        else:
            lis[i] = 0
            Evaluator._binary_strings_of_length(collect, lis, i+1, n)
            lis[i] = 1
            Evaluator._binary_strings_of_length(collect, lis, i+1, n)

    @staticmethod
    def binary_strings_of_length(n):
        collect = []
        Evaluator._binary_strings_of_length(collect, [0]*n, 0, n)
        return collect

    @staticmethod
    def _eval_for_assignment(expression, assignment):
        stack = deque()
        for x in expression:
            if x in Evaluator.VARS:
                stack.append(assignment[x])
            else:
                vars_consumption, func = Evaluator.OP[x]
                stack.append(func(*(stack.pop() for _ in range(vars_consumption))))
        return stack[0]

    @staticmethod
    def eval(expression):
        var_sym = Evaluator.get_vars_from_expression(expression)
        for v in Evaluator.binary_strings_of_length(len(var_sym)):
            if not Evaluator._eval_for_assignment(reversed(expression), dict(zip(var_sym,v))):
                return Evaluator.FAILURE
        return Evaluator.SUCCESS

def get_all_expressions_from_input():
    while True:
        exp = input()
        if exp == '0':
            break
        yield exp

def main():
    print('\n'.join(Evaluator.eval(exp) for exp in get_all_expressions_from_input()))

if __name__ == "__main__":
    main()