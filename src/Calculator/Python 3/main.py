import sys
for line in sys.stdin:
    print('%.2f' % eval(line))

# The non-lazy way... use two stacks (op and val)