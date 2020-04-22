def test_case(n):
    tracker, run, best = {}, 0, 0
    for i in range(n):
        k = int(input())
        if k not in tracker:
            tracker[k] = i
            run += 1
        else:
            run = min(run + 1, i - tracker[k])
            tracker[k] = i
        best = max(run, best)
    print(best)

def main():
    for _ in range(int(input())):
        test_case(int(input()))

if __name__ == "__main__":
    main()
