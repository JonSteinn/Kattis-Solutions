import sys

def sign(clerks):
    counter = 0
    while clerks:
        counter += 1
        i = 1
        for i in range(1,len(clerks)):
            if clerks[i-1] > clerks[i]:
                break
            elif i == len(clerks)-1:
                i += 1
        clerks = clerks[i:]
    return counter

def main():
    print(sign(list(map(int, sys.stdin.readlines()[1:]))))


if __name__ == "__main__":
    main()