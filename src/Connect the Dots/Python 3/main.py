import sys

class Order:
    MAP = {}

    @staticmethod
    def initialize():
        value = 0
        for i in range(10):
            Order.MAP[chr(ord('0')+i)] = value
            value += 1
        for i in range(26):
            Order.MAP[chr(ord('a')+i)] = value
            value += 1
        for i in range(26):
            Order.MAP[chr(ord('A')+i)] = value
            value += 1

    @staticmethod
    def value_of(symbol):
        return Order.MAP[symbol]

    @staticmethod
    def is_symbol(symbol):
        return symbol in Order.MAP

def connect(mat, src, dst):
    s_r, s_c, d_r, d_c = *src,*dst
    if s_r != d_r:
        for r in range(min(s_r,d_r)+1,max(s_r,d_r)):
            if mat[r][s_c] == '.':
                mat[r][s_c] = '|'
            elif mat[r][s_c] == '-':
                mat[r][s_c] = '+'
    else:
        for c in range(min(s_c,d_c)+1,max(s_c,d_c)):
            if mat[s_r][c] == '.':
                mat[s_r][c] = '-'
            elif mat[s_r][c] == '|':
                mat[s_r][c] = '+'
    
def connect_board(mat, symbols):
    last = None
    for symbol in sorted(symbols.keys(),key=lambda z: Order.value_of(z)):
        if last is not None:
            connect(mat, symbols[last], symbols[symbol])
        last = symbol

def find_symbols(mat):
    positions = {}
    for r,row in enumerate(mat):
        for c,symbol in enumerate(row):
            if Order.is_symbol(symbol):
                positions[symbol] = (r,c)
    return positions 

def process_board(mat):
    symbols = find_symbols(mat)
    connect_board(mat, symbols)
    print('\n'.join((''.join(r) for r in mat)))
    mat.clear()

def main():
    Order.initialize()
    mat = []
    for line in sys.stdin:
        if line == '\n':
            process_board(mat)
            print()
        else:
            mat.append(list(line.rstrip()))
    process_board(mat)

if __name__ == "__main__":
    main()