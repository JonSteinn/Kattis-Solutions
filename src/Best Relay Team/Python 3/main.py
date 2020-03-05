from itertools import combinations

def find_best(lis):
    # Combine top 4 in each category, then small enough to
    # bruteforce [at most 8 => 8*(8 choose 3) iterations].
    draft = set(sorted(lis, key=lambda x: x[1])[:4]+sorted(lis, key=lambda x: x[2])[:4])
    best = [100000, '', '', '', '']
    for first in draft:
        for rest in combinations(draft - {first}, 3):
            time = first[1] + sum(x[2] for x in rest)
            if time < best[0]:
                best[0] = time
                best[1] = first[0]
                for i,r in enumerate(rest):
                    best[i+2] = r[0]
    best[0] = '%.9f' % best[0]
    return best

def main():
    lis = [(lambda a,b,c: (a, float(b), float(c)))(*tuple(input().split())) for _ in range(int(input()))]
    print('\n'.join(find_best(lis)))

if __name__ == "__main__":
    main()