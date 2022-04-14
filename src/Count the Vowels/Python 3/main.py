from collections import Counter

print((lambda cnt: sum(cnt[x] for x in 'aAeEiIoOuU'))(Counter(input())))