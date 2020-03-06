h,v = tuple(input().split())

for i,c in enumerate(h):
    j = v.find(c)    
    if j != -1:
        break
    
for y in range(len(v)):
    if y == j:
        print(h)
    else:
        print('.' * i + v[y] + '.' * (len(h)-i-1))