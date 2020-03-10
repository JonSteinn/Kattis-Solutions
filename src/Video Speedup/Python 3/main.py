n,p,k = map(int, input().split())
times = [0]+list(map(int, input().split()))+[k]
print(sum((1+p*i/100) * (times[i+1]-times[i]) for i in range(n+1)))