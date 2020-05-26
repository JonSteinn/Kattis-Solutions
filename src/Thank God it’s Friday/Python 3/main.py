from datetime import datetime

def get_input():
    d,m = input().split()
    return (
        int(d),
        {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}[m],
        {'MON': 0, 'TUE': 1, 'WED': 2, 'THU': 3, 'FRI': 4, 'SAT': 5, 'SUN': 6}[input()]
    )

def is_friday(start, stop, wd):
    return (wd + (stop-start).days) % 7 == 4

def friday_check(d,m,wd):
    try:
        if is_friday(datetime(year=2000, month=1, day=1),datetime(year=2000, month=m, day=d),wd):
            if m == 2 and d == 29:
                return 'TGIF'
            elif is_friday(datetime(year=2001, month=1, day=1),datetime(year=2001, month=m, day=d),wd):
                return 'TGIF'
            else:
                return 'not sure'
        else:
            if is_friday(datetime(year=2001, month=1, day=1),datetime(year=2001, month=m, day=d),wd):
                return 'not sure'
            else:
                return ':('
    except:
        return ':(' # Invaldi date?

def main():
    d,m,wd = get_input()
    print(friday_check(d,m,wd))

if __name__ == "__main__":
    main()