import itertools
print((lambda n, m: (lambda a, b: "\n".join(itertools.chain(('*' * (a+1) for _ in range(b)), ('*' * a for _ in range(n-b)))))(*divmod(m, n)))(int(input()), int(input())))