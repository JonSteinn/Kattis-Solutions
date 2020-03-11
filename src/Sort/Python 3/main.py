from collections import defaultdict

def main():
    input() # dump
    first_appearance = {}
    counter = defaultdict(lambda: 0)
    numbers = input().split()
    for i,x in enumerate(numbers):
        counter[x] += 1
        if x not in first_appearance:
            first_appearance[x] = i
    print(' '.join(sorted(numbers, key=lambda z: (-counter[z],first_appearance[z]))))

if __name__ == "__main__":
    main()