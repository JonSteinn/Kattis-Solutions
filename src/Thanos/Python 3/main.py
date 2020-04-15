def test_case(p,r,f):
    counter = 0
    while p <= f:
        p *= r
        counter += 1
    print(counter)

def main():
    for _ in range(int(input())):
        test_case(*map(int,input().split()))

if __name__ == "__main__":
    main()