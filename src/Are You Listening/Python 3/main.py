from math import sqrt

print(max(0,int((lambda x,y,n: sorted((lambda a,b,r: sqrt((x-a)**2 + (y-b)**2) - r)(*map(int, input().split())) for _ in range(n)))(*map(int,input().split()))[2])))