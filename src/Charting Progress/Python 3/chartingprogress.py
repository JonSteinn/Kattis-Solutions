import sys

total = 0
for line in sys.stdin:
    if line == '\n':
        total = 0
        print()
    else:
        n = line.count('*')
        l = len(line) - 1
        print(('.' * (l - n - total)) + ('*' * n) + ('.' * total))
        total += n