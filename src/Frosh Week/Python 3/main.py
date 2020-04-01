def merge(cpy,l,m,r,arr):
    inv,i,j = 0,l,m
    for k in range(l, r):
        if i < m and (j >= r or cpy[i] <= cpy[j]):
            arr[k] = cpy[i]
            i += 1
        else:
            if i < m:
                inv += (m-i)
            arr[k] = cpy[j]
            j += 1
    return inv

def merge_sort(arr, l, r, cpy):
    if r - l < 2:
        return 0
    m = (l+r)//2
    return merge_sort(cpy, l, m, arr) + merge_sort(cpy, m, r, arr) + merge(arr, l, m, r, cpy)

def inversions(lis):
    return merge_sort(lis,0,len(lis),lis.copy())

def main():
    print(inversions([int(input()) for _ in range(int(input()))]))

if __name__ == "__main__":
    main()