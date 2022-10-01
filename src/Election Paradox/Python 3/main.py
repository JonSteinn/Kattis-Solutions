n = int(input())
regions = sorted(map(int, input().split()))
votes = 0

for _ in range((n-1)//2):
    votes += regions.pop()
votes += sum((pop // 2 for pop in regions))
print(votes)