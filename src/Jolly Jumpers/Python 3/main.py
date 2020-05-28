from sys import stdin

print('\n'.join((lambda n, *lis: 'Jolly' if len({abs(a-b) for a,b in zip(lis,lis[1:]) if 0<abs(a-b)<n}) == n-1 else 'Not jolly')(*map(int,line.split())) for line in stdin))