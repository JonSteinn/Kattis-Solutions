from math import log2 as lg

def main():
    n,k = map(int,input().split())
    if k >= lg(n):
        print('Your wish is granted!')
    else:
        print('You will become a flying monkey!')

if __name__ == "__main__":
    main()