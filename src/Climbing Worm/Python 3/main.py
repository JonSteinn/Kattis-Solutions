def climb(a,b,h):
    c,y = 0,0
    while True:
        y += a
        c += 1
        if y >= h:
            return c
        y -= b

def main():
    print(climb(*map(int,input().split())))

if __name__ == "__main__":
    main()