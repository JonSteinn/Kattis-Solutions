def score(arr):
    return (sum(x*0.8**i for i,x in enumerate(arr))/5)

def main():
    n = int(input())
    scores = [int(input()) for _ in range(n)]
    print('%.6f' % score(scores))
    print('%.6f' % (sum(score(scores[:i]+scores[i+1:]) for i in range(n))/n))

if __name__ == "__main__":
    main()