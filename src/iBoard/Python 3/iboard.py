import sys

print('\n'.join(['trapped' if (lambda x, y: (x & 1) or (y & 1))(*((lambda a, b: (a - b, b))(*((lambda l: (len(l), sum(bin(ord(c))[2:].count('1') for c in l)))(line[:-1]))))) else 'free' for line in sys.stdin]))