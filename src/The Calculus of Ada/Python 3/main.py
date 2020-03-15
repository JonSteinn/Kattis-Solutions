def extend(arr):
    Mat = [arr]
    n = Mat[0].pop(0)
    while n > 1 and any(x != Mat[-1][0] for x in Mat[-1]):
        Mat.append([Mat[-1][i+1]-Mat[-1][i] for i in range(n-1)])
        n -= 1
    return len(Mat)-1, sum(row[-1] for row in Mat)

print(*extend(list(map(int, input().split()))))