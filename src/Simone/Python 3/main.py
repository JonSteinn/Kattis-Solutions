_, k = input().split()
k = int(k)
counter = [0]*k
for color in map(int, input().split()):
    counter[color - 1] += 1
min_ = min(counter)
least_common = sorted((i + 1 for i, cnt in enumerate(counter) if cnt == min_))
print(len(least_common))
print(" ".join(map(str, least_common)))