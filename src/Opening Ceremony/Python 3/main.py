from collections import Counter

def cuts(n,heights):
    best = n
    x = 0
    for h in sorted(heights.keys()):
        x += heights[h]
        best = min(best, h + n - x)
    return best

def main():
    n = int(input())
    heights = Counter(map(int,input().split()))
    print(cuts(n,heights))
    
if __name__ == "__main__":
    main()