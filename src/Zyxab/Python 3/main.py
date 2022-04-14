import collections 

best = None
for name in range(int(input())):
    curr = input()
    if len(curr) > 4 and collections.Counter(curr).most_common()[0][1] == 1 and (best is None or len(curr) < len(best) or (len(curr) == len(best) and curr > best)):
        best = curr
print("neibb!" if best is None else best)