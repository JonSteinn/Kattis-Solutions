
m,n = tuple(map(int, input().split()))
u,l,r,d = tuple(map(int, input().split()))

width = n+l+r
height = m+u+d
rows = ['#.' * (width // 2) + ('#' if width % 2 == 1 else ''),'.#' * (width // 2) + ('.' if width % 2 == 1 else '')]
mat = [rows[i%2] for i in range(height)]

for i in range(u,u+m):
    mat[i]  = mat[i][:l] + input() + mat[i][(l+n):]

print('\n'.join(mat))