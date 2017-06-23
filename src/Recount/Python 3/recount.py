from collections import defaultdict

votes = defaultdict(lambda: 0)
while True:
    s = input()
    if s == '***':
        break
    votes[s] = votes[s] + 1
sorted_voted = sorted(list(votes.items()), key=lambda z: z[1], reverse=True)
if len(sorted_voted) == 1 or sorted_voted[0][1] != sorted_voted[1][1]:
    print(sorted_voted[0][0])
else:
    print("Runoff!")