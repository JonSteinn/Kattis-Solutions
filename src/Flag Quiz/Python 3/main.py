def fill_dist(n):
    diff = [[0] * n for _ in range(n)]
    options = []
    for i in range(n):
        options.append(input().split(', '))
        for j in range(i):
            d = sum(a != b for a, b in zip(options[i],options[j]))
            diff[i][j] = d
            diff[j][i] = d
    return diff,options

def find_best(diff):
    least,least_i = 2147483647, []
    for i, row in enumerate(diff):
        s = max(row)
        if s == least:
            least_i.append(i)
        elif s < least:
            least_i = [i]
            least = s
    return least_i

def main():
    input()
    n = int(input())
    diff,options = fill_dist(n)
    best = find_best(diff)
    print('\n'.join((', '.join(options[i]) for i in best)))

if __name__ == "__main__":
    main()