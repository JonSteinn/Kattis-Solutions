sum_, min_ = 0, 0
for _ in range(int(input())):
    sum_ += int(input())
    min_ = min(sum_, min_)
print(max(-min_, 0))