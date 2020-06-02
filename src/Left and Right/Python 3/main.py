def path(p):
    l,r = 1,1
    for x in p:
        if x == 'R':
            for i in range(r,l-1,-1):
                yield str(i)
            l = r+1
        r += 1
    for i in range(r,l-1,-1):
        yield str(i)

def main():
    input()
    print('\n'.join(p for p in path(input())))

if __name__ == "__main__":
    main()