
def dist_squared(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

def find_place(hatches, s):
    for x in range(1, s+1):
        for y in range(1, s+1):
            if (x,y) not in hatches and all(dist_squared(x,y,*h) <= min(min(x, s-x)**2, min(y, s-y)**2) for h in hatches):
                return f'{x} {y}'
    return 'poodle'

def test_case(s,h):
    print(find_place(set(tuple(map(int, input().split())) for _ in range(h)), s))

def main():
    for _ in range(int(input())):
        test_case(*tuple(map(int, input().split())))

if __name__ == "__main__":
    main()