def key_press(p,k,l,freq):
    s = 0
    for i in range(1,p+1):
        for _ in range(k):
            if freq:
                s += i*freq.pop(0)
            else:
                return s
    return s

def main():
    for i in range(int(input())):
        p,k,l = map(int,input().split())
        freq = sorted(map(int, input().split()),reverse=True)
        print(f'Case #{i+1}: {key_press(p,k,l,freq)}')

if __name__ == "__main__":
    main()