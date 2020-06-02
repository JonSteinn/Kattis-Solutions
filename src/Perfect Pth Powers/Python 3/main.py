from math import sqrt, gcd

def min_power_helper(x):
    div_cnt = 0
    while x%2 == 0:
        x //= 2
        div_cnt += 1
    if div_cnt == 1:
        return 1
    
    g = -1 if div_cnt == 0 else div_cnt
    div_cnt = 0

    while x%3 == 0:
        x //= 3
        div_cnt += 1
    if div_cnt == 1:
        return 1

    g = -1 if g < 0 and div_cnt == 0 else (div_cnt if g == -1 else gcd(g, div_cnt))

    if g == 1 or x == 1:
        return g

    f, top, jump = 5, sqrt(x), 2
    while f <= top:
        if x % f == 0:
            div_cnt = 0
            while x % f == 0:
                div_cnt += 1
                x //= f
            if g == -1:
                g = div_cnt
            else:
                g = gcd(g, div_cnt)
            if g == 1:
                return g
        f = f + jump
        jump = 2 if jump == 4 else 4

    if x > 1:
        return 1

    return g

def min_power(x):
    return str((lambda m: m >> ((m&(-m)).bit_length()-1))(min_power_helper(-x)) if x < 0 else min_power_helper(x))

def get_input():
    while True:
        x = int(input())
        if x:
            yield x
        else:
            break

def main():
    print('\n'.join(min_power(x) for x in get_input()))

if __name__ == "__main__":
    main()