print(sum(int(a == b) for a,b in (lambda lis: zip(lis, lis[1:]))([input() for _ in range(int(input()))])))