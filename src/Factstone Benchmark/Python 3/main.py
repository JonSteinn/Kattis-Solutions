from math import log2 as lg

# max {n : N! < 2**bits}
# => # lg(1)+lg(2)+...+lg(n) < bits
def pre_process():
    years_to_bits = {y: 2**(i+2) for i,y in enumerate(range(1960,2170,10))}
    years_to_n = {}
    s,n,year = 0,2,1960
    while year < 2170:
        s += lg(n)
        if s > years_to_bits[year]:
            years_to_n[year] = n-1
            year += 10
        n += 1
    return years_to_n

def main():
    years_to_n = pre_process()
    while True:
        n = int(input())
        if n == 0:
            break
        print(years_to_n[n - n%10])

if __name__ == "__main__":
    main()
