def seq(prev):
    i = 2
    while True:
        curr = len(str(prev))
        if curr == prev:
            return i
        else:
            i += 1
            prev = curr

def main():
    while True:
        n = input()
        if n == 'END':
            break
        l = len(n)
        if l < 8 and int(n) == l:
            print(1)
        else:
            print(seq(l))

if __name__ == "__main__":
    main()