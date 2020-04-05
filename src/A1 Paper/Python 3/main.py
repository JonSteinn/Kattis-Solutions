def sides(n):
    ratio = 0.70710678118654746171500846685376018285751342773438 # 2^(-1/2)
    arr = [(
        0.42044820762685725101803768666286487132310867309570, # 2^(-5/4)
        0.59460355750136051344867382795200683176517486572266  # 2^(-3/4)
    )]
    while len(arr) < n:
        arr.append((lambda z: (ratio*z, z))(arr[-1][0]))
    return arr

def merge(arr,s):  
    needed = 2-arr[0]
    for i,x in enumerate(arr[1:]):
        if x >= 2*needed:
            arr[i+1] -= 2*needed
            arr[i] += needed
            return True, needed * s[i+1][1]
        else:
            needed = (2*needed - x)
    return False, 0.0

def tape(n, arr):
    length = 0.0
    s = sides(n-1)
    while arr and arr[0] < 2:
        m, l = merge(arr, s)
        length += l
        if not m:
            break
    return -1.0 if not arr or arr[0] < 2 else s[0][1] + length

def trim_right(n,arr):
    while arr and arr[-1] == 0:
        n -= 1
        arr.pop()
    return n

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    n = trim_right(n,arr)
    t = tape(n, arr)
    if t < 0:
        print('impossible')
    else:
        print(t)

if __name__ == "__main__":
    main()
