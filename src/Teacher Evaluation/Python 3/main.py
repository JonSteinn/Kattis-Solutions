def get_number_of_full_scores(n,s,p):
    a,b = n*p-s, 100-p
    d,m = divmod(a,b)
    return d if m else d-1

def test_to_add(n,s,p):
    if p == 100:
        return 'impossible' if 100*n != s else 0
    k = get_number_of_full_scores(n,s,p)
    s += 100*k
    expected_sum = (n+k)*p
    if expected_sum == s:
        return k
    for i in range(1,100):
        if s + i == expected_sum:
            return k+1
    return 'impossible'

def main():
    (n,p),s = map(int,input().split()),sum(map(int,input().split()))
    print(test_to_add(n,s,p))

if __name__ == "__main__":
    main()