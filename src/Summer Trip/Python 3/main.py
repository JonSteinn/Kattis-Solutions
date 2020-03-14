def ones(n): 
    count = 0
    while n: 
        n &= (n-1)
        count += 1
    return count

def count(w):
    counter = 0
    since_last = (lambda z: [1<<z]*z + [0] + [1<<z]*(25-z))(ord(w[0])-97)
    for char in w[1:]:
        val = ord(char)-97
        counter += ones(since_last[val])
        for i in range(26):
            since_last[i] |= 1 << val
        since_last[val] = 0
    return counter

print(count(input()))