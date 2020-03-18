
from math import pi

def main():
    A,N = map(float, input().split())

    if N**2 / (4*pi) >= A:
        print('Diablo is happy!')
    else:
        print('Need more materials!')

if __name__ == "__main__":
    main()