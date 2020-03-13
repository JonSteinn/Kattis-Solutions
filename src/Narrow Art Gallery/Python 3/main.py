# Using .__setitem__ since Kattis is using py3.6 when I'm solving 
# this and assignment within lambda is invald until 3.8

# I cleaned my original code before 'onelinerfying' it but didn't 
# saved it so I'll throw the original solution below, although 
# somewhat tedious (not using bitmasks)

# TODO: Anonymous recursion to combine... 
def optimal_blockage(mat, n, k, prev_col, recursive_memory):
    return 0 if n < k or n == 0 or k==0 else (lambda x: recursive_memory.__setitem__((n,k,prev_col),x) or x)(min(sum(mat[i][j] for i in range(k)) for j in range(2) if prev_col & (1<<j) != 0) if n == k else min(min(optimal_blockage(mat, n-1, k-1, prev_col=j+1,recursive_memory=recursive_memory) + mat[n-1][j] for j in range(2) if prev_col & (1<<j) != 0),optimal_blockage(mat, n-1, k,3,recursive_memory=recursive_memory))) if (n,k,prev_col) not in recursive_memory else recursive_memory[(n,k,prev_col)]

print((lambda a,b,c: sum(sum(a,[]))-optimal_blockage(a,b,c,3,{}))(*(lambda d, _: d)((lambda a, b: ([list(map(int, input().split())) for _ in range(a)], a, b))(*map(int, input().split())),input())))


"""
recursive_memory = {}

def recursive_helper(mat, n, k, prev_col = -1):
    if n < k or n == 0 or k==0:
        return 0
    if (n,k,prev_col) not in recursive_memory:
        if n == k:
            if prev_col == -1:
                recursive_memory[(n,k,prev_col)] = min(sum(mat[i][0] for i in range(k)),sum(mat[i][1] for i in range(k)))
            elif prev_col == 0:
                recursive_memory[(n,k,prev_col)] = sum(mat[i][1] for i in range(k))
            else:
                recursive_memory[(n,k,prev_col)] = sum(mat[i][0] for i in range(k))
        else:
            l,r = mat[n-1]
            if prev_col == -1:
                recursive_memory[(n,k,prev_col)] = min(
                    recursive_helper(mat, n-1, k),
                    recursive_helper(mat, n-1, k-1, prev_col=0) + l,
                    recursive_helper(mat, n-1, k-1, prev_col=1) + r
                )
            elif prev_col == 0:
                recursive_memory[(n,k,prev_col)] = min(
                    recursive_helper(mat, n-1, k),
                    recursive_helper(mat, n-1, k-1, prev_col=0) + l
                )
            else:
                recursive_memory[(n,k,prev_col)] = min(
                    recursive_helper(mat, n-1, k),
                    recursive_helper(mat, n-1, k-1, prev_col=1) + r
                )
    return recursive_memory[(n,k,prev_col)]

def optimal_blockage(mat, n, k):
    return  recursive_helper(mat, n, k)

def main():
    n,k = map(int, input().split())
    s, mat = (0,list())
    for _ in range(n):
        mat.append(list(map(int, input().split())))
        s += sum(mat[-1])
    input() # Dump last line
    print(s - optimal_blockage(mat,n,k))

if __name__ == "__main__":
    main()
"""