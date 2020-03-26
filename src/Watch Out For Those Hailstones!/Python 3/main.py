def h_sum(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + h_sum(n//2)
    return n + h_sum(3*n+1)

def main():
    n = int(input())
    print(h_sum(n))

if __name__ == "__main__":
    main()