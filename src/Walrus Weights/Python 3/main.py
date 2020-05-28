import sys 
  
sys.setrecursionlimit(1_000_000) 

def best_fit_rec(t,i,n,w,mem):
    if i == n-1:
        return 0 if t < abs(t-w[i]) else w[i]
    if mem[t][i] == -1:
        if w[i] > t:
            incl = w[i]
        else:
            incl = w[i] + best_fit_rec(t-w[i],i+1,n,w,mem)
        excl = best_fit_rec(t,i+1,n,w,mem)
        a1,a2 = abs(t-incl),abs(t-excl)
        if a1 == a2:
            mem[t][i] = max(incl,excl)
        elif a1 < a2:
            mem[t][i] = incl
        else:
            mem[t][i] = excl
    return mem[t][i]

def best_fit(weights):
    return best_fit_rec(1000,0,len(weights),weights,[[-1]*1001 for _ in range(1001)])

def weights():
    for _ in range(int(input())):
        yield int(input())

def main():
    print(best_fit([_w for _w in weights()]))


if __name__ == "__main__":
    main()