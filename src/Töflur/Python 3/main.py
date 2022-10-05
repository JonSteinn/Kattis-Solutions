_ = input()
numbers = sorted(map(int, input().split()), reverse=True)
print(sum((a-b)**2 for a, b in zip(numbers, numbers[1:])))