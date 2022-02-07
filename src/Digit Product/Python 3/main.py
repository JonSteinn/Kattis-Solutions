import functools
import operator

def find(n):
    return n if n < 10 else find(functools.reduce(operator.mul, (int(d) for d in str(n) if d != '0')))

def main():
    print(find(int(input())))

if __name__ == "__main__":
    main()
