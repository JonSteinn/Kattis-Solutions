_ = input()
print(set(map(int, input().split())).difference(map(int, input().split())).pop())