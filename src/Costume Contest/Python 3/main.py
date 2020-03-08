from collections import defaultdict

costumes = defaultdict(lambda: 0)
for _ in range(int(input())):
    costumes[input()] += 1
costumes = sorted(costumes.items(), key=lambda z: (z[1],z[0]))
for costume, count in costumes:
    if count == costumes[0][1]:
        print(costume)
    else:
        break
