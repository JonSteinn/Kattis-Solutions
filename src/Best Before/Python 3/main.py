from itertools import permutations
from datetime import datetime

def add_time(times, y, m, d):
    y = '2000'[:4-len(y)] + y
    try:
        d = datetime(int(y),int(m),int(d))
    except ValueError:
        return
    if datetime(2000,1,1) <= d <= datetime(2999,12,31):
        times.append(d)

def main():
    inp, times = input(), []
    for a,b,c in permutations(inp.split('/'),3):
        add_time(times, a, b, c)
    if times:
        print(sorted(times)[0].strftime('%Y-%m-%d'))
    else:
        print(f'{inp} is illegal')
        
if __name__ == "__main__":
    main()