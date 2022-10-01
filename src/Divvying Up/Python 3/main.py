_ = input()
print(["yes", "no"][bool(sum(map(int, input().split())) % 3)])