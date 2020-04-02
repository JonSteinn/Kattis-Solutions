def quickest(q,m,s,l):
    total = 0
    if l >= m:
        total += (l // m)*q
        l %= m
    if l == 0:
        if s == 0:
            return total
        total += (s//m)
        return total + (0 if s % m == 0 else 1)
    total += q
    if s <= (m-l)*q:
        return total
    s -= (m-l)*q
    total += (s//m)
    return total + (0 if s % m == 0 else 1)


def main():
    print(quickest(*map(int,input().split())))

if __name__ == "__main__":
    main()