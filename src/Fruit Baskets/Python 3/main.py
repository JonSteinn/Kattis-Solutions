from itertools import islice

def all_weights(lis,i,n,included):
    if i == n-1:
        included[i] = True
        a = sum(lis[j] for j in range(i+1) if included[j])
        if a < 200:
            return 0
        included[i] = False
        b = sum(lis[j] for j in range(i+1) if included[j])
        if b < 200:
            return a
        else:
            return b
    else:
        included[i] = True
        z = sum(lis[j] for j in range(i+1) if included[j])
        if z >= 200:
            b = 2**(n-i-2) * (2*z+sum(islice(lis, i+1, None)))
        else:
            b = all_weights(lis,i+1,n,included)
        included[i] = False
        z = sum(lis[j] for j in range(i+1) if included[j])
        if z >= 200:
            a = 2**(n-i-2) * (2*z+sum(islice(lis, i+1, None)))
        else:
            a = all_weights(lis,i+1,n,included)
        return a+b

def main():
    n = int(input())
    lis = sorted(map(int,input().split()),reverse=True)
    print(all_weights(lis,0,n,[False]*n))

if __name__ == "__main__":
    main()
