from collections import defaultdict

MOD = 1_000_000_007

def meanings(w,d,i,n,mem = {}):
    if i > n:
        return 1
    if i not in mem:    
        s = 0
        for part,k in d[w[i]].items():
            if w[i:].startswith(part):
                s = (s + k * meanings(w,d,i+len(part),n,mem)) % MOD
        mem[i] = s 
    return mem[i]

def main():
    n, w = input().split()
    d = defaultdict(dict)
    for _ in range(int(n)):
        a,b = input().split()
        d[a[0]][a] = int(b)
    print(meanings(w,d,0,len(w)-1))

if __name__ == "__main__":
    main()