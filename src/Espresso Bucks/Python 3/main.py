def place_coffee_shops(mat,r,c,s):
    while s:
        _r,_c = s.pop()
        mat[_r][_c] = 'E'
        s.discard((_r-1,_c))
        s.discard((_r+1,_c))
        s.discard((_r,_c-1))
        s.discard((_r,_c+1))

def find_possible(mat):
    s=set()
    for r,row in enumerate(mat):
        for c,x in enumerate(row):
            if x == '.':
                s.add((r,c))
    return s

def main():
    r,c = map(int,input().split())
    mat = [list(input()) for _ in range(r)]
    s = find_possible(mat)
    place_coffee_shops(mat,r,c,s)
    print('\n'.join(''.join(x for x in row) for row in mat))

if __name__ == "__main__":
    main()