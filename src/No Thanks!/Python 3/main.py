_ = input()
cards = sorted(map(int, input().split()))
last, curr = None, None
score = 0
while cards:
    last, curr = curr, cards.pop()
    if last is not None and curr == last - 1:
        score -= last
    score += curr
print(score)