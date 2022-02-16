n,k,p = map(float, input().split())
print("spela" if -k * (1-p) + (n-k)*p < 0 else "spela inte!")