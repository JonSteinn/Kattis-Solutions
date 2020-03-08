total, mario = tuple(map(int, input().split()))
mario = {int(input()) for _ in range(mario)}
for i in range(total):
    if i not in mario:
        print(i)
print(f'Mario got {len(mario)} of the dangerous obstacles.')