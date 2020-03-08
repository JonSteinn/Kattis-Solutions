from itertools import permutations
from heapq import heappop, heappush

days = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9:30, 10: 31, 11: 30, 12: 31}

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return days[month]

def is_valid(d,m,y):
    if y < 2000:
        return False
    if m == 0 or m > 12:
        return False
    if d == 0 or d > days_in_month(m, y):
        return False
    return True

def print_heap(heap):
    n = len(heap)
    if n == 0:
        print('0')
    else:
        y,m,d = heappop(heap)
        m = f'0{m}' if m < 10 else f'{m}'
        d = f'0{d}' if d < 10 else f'{d}'
        print(f'{n} {d} {m} {y}')

def test_case():
    visited = set()
    heap = []
    # Problem gives 4s to run and 50 * 8! = 50 * 40320 = 2016000 so bruteforce will do
    for p in permutations(input().replace(' ', '')):
        d,m,y = (lambda s: (int(s[:2]),int(s[2:4]),int(s[4:])))(''.join(p))
        if not is_valid(d,m,y) or (d,m,y) in visited:
            continue
        visited.add((d,m,y))
        heappush(heap, (y,m,d))
    print_heap(heap)

def main():
    for _ in range(int(input())):
        test_case()

if __name__ == "__main__":
    main()