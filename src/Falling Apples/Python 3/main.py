def col_sim(r,c,mat):
    while r > 0:
        if mat[r][c] == '.':
            offset = 0
            _r = r-1
            while True:
                if _r < 0:
                    return
                if mat[_r][c] == '#':
                    r = _r - 1
                    break
                elif mat[_r][c] == 'a':
                    mat[_r][c] = '.'
                    mat[r-offset][c] = 'a'
                    offset += 1
                _r -= 1
        else:
            r -= 1

def simulate(r,c,mat):
    for i in range(c):
        col_sim(r-1,i,mat)

def main():
    r,c = map(int,input().split())
    mat = [list(input()) for _ in range(r)]
    simulate(r,c,mat)
    print('\n'.join(''.join(char for char in row) for row in mat))

if __name__ == "__main__":
    main()