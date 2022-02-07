n, s = int(input()), 0
while n:    
    start = int(input())
    if n == 1:
        print("still running")
        break
    s += int(input()) - start
    n -= 2
else:
    print(s)
