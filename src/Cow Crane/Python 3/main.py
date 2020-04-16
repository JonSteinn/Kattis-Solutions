def start_with_m(m,l,M,L,t_m,t_l):
    init_time_m = abs(m) + abs(m-M)
    latter_time_l = init_time_m + abs(M-l) + abs(l-L)
    return init_time_m <= t_m and latter_time_l <= t_l

def start_with_l(m,l,M,L,t_m,t_l):
    init_time_l = abs(l) + abs(l-L)
    latter_time_m = init_time_l + abs(L-m) + abs(m-M)
    return init_time_l <= t_l and latter_time_m <= t_m
    
def possible(m,l,M,L,t_m,t_l):
    if any((start_with_m(m,l,M,L,t_m,t_l),start_with_l(m,l,M,L,t_m,t_l))):
        return True
    if m < l <= 0:
        return start_with_m(m, m, M, L, t_m, t_l)
    if 0 <= l < m:
        return start_with_m(m, m, M, L, t_m, t_l)
    if l < m <= 0:
        return start_with_l(l, l, M, L, t_m, t_l)
    if 0 <= m < l:
        return start_with_l(l, l, M, L, t_m, t_l)
    return False

def main():
    print('possible' if possible(*map(int,input().split()),*map(int,input().split()),*map(int,input().split())) else 'impossible')

if __name__ == "__main__":
    main()