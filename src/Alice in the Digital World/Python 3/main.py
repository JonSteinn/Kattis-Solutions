def max_weight(lo, weights):
    best, pre, run = (0,)*3
    for w in weights:
        if w < lo:
            best = max(best, run + pre if run else 0)
            pre, run = 0, 0
        elif w == lo:
            best = max(best, run + pre if run else 0)
            run = lo + pre
            pre = 0
        else:
            pre += w
    return max(best, run + pre) if run else best

def main():
    print('\n'.join(str(max_weight(int(input().split()[1]), map(int,input().split()))) for _ in range(int(input()))))

if __name__ == "__main__":
    main()