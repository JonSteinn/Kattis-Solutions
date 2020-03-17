def divisors(n):
    lis = [1]
    if n < 0:
        n = -n
    f,step = (2,1) if n%2==0 else (3,2)
    while f*f <= n:
        if n % f == 0:
            lis.append(f)
            rem = n//f
            if rem != f:
                lis.append(rem)
        f += step
    lis.append(n)
    return lis

def find_best(n):
    best = 2147483647
    divs = divisors(n)
    for i,s1 in enumerate(divs):
        for s2 in divs[i:]:
            prod = s1*s2
            if n%prod == 0:
                s3 = n//prod
                area = 2*s1*s2+2*s1*s3+2*s2*s3
                if area < best:
                    best = area
    return best

def main():
    n = int(input())
    print(find_best(n))

if __name__ == "__main__":
    main()