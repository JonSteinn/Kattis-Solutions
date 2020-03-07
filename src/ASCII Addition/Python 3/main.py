ascii = {
    'xxxxxxxx.....xx.....xx.....xxxxxxxx': '0',
    '............................xxxxxxx': '1',
    'x..xxxxx..x..xx..x..xx..x..xxxxx..x': '2',
    'x..x..xx..x..xx..x..xx..x..xxxxxxxx': '3',
    'xxxx......x......x......x...xxxxxxx': '4',
    'xxxx..xx..x..xx..x..xx..x..xx..xxxx': '5',
    'xxxxxxxx..x..xx..x..xx..x..xx..xxxx': '6',
    'x......x......x......x......xxxxxxx': '7',
    'xxxxxxxx..x..xx..x..xx..x..xxxxxxxx': '8',
    'xxxx..xx..x..xx..x..xx..x..xxxxxxxx': '9',
    '...x......x....xxxxx....x......x...': '+'
}

digits = {
    '0': ['xxxxx', 'x...x', 'x...x', 'x...x', 'x...x', 'x...x', 'xxxxx'],
    '1': ['....x', '....x', '....x', '....x', '....x', '....x', '....x'],
    '2': ['xxxxx', '....x', '....x', 'xxxxx', 'x....', 'x....', 'xxxxx'],
    '3': ['xxxxx', '....x', '....x', 'xxxxx', '....x', '....x', 'xxxxx'],
    '4': ['x...x', 'x...x', 'x...x', 'xxxxx', '....x', '....x', '....x'],
    '5': ['xxxxx', 'x....', 'x....', 'xxxxx', '....x', '....x', 'xxxxx'],
    '6': ['xxxxx', 'x....', 'x....', 'xxxxx', 'x...x', 'x...x', 'xxxxx'],
    '7': ['xxxxx', '....x', '....x', '....x', '....x', '....x', '....x'],
    '8': ['xxxxx', 'x...x', 'x...x', 'xxxxx', 'x...x', 'x...x', 'xxxxx'],
    '9': ['xxxxx', 'x...x', 'x...x', 'xxxxx', '....x', '....x', 'xxxxx'],
}

def number_to_ascii(n):
    print('\n'.join('.'.join(digits[c][i] for c in n) for i in range(7)))

def calculate_input():
    lines = [input() for _ in range(7)]
    n = len(lines[0])
    transpose = list(map(lambda z: ''.join(z), zip(*map(tuple, lines))))
    return str(eval(''.join(ascii[''.join(transpose[i:i+5])] for i in range(0,n,6))))

def main():
    number_to_ascii(calculate_input())

if __name__ == "__main__":
    main()