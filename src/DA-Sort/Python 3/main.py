def sorter(arr):
    lo,min_to_move, mtm_i,to_move = (1000000001,1000000001,len(arr),set())

    # Find all with a smaller element to their right
    for i,c in enumerate(reversed(arr)):
        if c > lo:
            to_move.add(len(arr)-1-i)
            if c <= min_to_move:
                min_to_move = c
                mtm_i = len(arr)-1-i
        else:
            lo = c

    # Special case when smallest to move is already at the end
    if arr[-1] == min_to_move:
        return len(to_move)

    # Anyone larger than the smallest to move, to its right, has
    # to be moved now, since moving the smallest would create
    # an inversion between it and any larger to its right (that is,
    # to its right in the original array, prior to the move). 
    for i,c in enumerate(arr[mtm_i+1:]):
        if c > min_to_move:
            to_move.add(mtm_i+1+i)

    return len(to_move)

def main():
    for i in range(int(input())):
        _,c = map(int,input().split())
        lis = []
        for _ in range(c // 10 + (1 if c % 10 > 0 else 0)):
            lis.extend(map(int,input().split()))
        ops = sorter(lis)
        print(f'{i+1} {ops}')

if __name__ == "__main__":
    main()

"""
# Bruteforce to generate test cases:

def sorter2(arr):
    #print('-----------------------------')
    #print(arr)
    #print()

    s = sorted(arr)

    i = 0
    j = 0
    c = 0
    while s != arr:
        if arr[i] == s[j]:
            i += 1
            j += 1
        else:
            i += 1
        
        if i == len(arr):
            x = arr.index(s[j])
            #print(f'MOVE {s[j]}')
            arr = arr[:x] + arr[x+1:] + [s[j]]
            #print(arr)
            #print()
            c += 1
            i = 0
            j = 0
    #print('-----------------------------')
    return c
"""