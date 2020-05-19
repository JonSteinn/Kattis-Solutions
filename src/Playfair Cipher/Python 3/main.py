from collections import deque

def create_key(key_phrase):
    all_chars = {chr(i+97) for i in range(26)}
    all_chars.remove('q')

    key = []
    for c in key_phrase:
        if c == ' ' or c not in all_chars:
            continue
        key.append(c)
        all_chars.remove(c)
    
    key.extend(sorted(all_chars))
    mat = [key[i:i + 5] for i in range(0, len(key), 5)]  
    d = {}
    for r,row in enumerate(mat):
        for c,x in enumerate(row):
            d[x] = (r,c)
    return mat,d

def encrypt(string, key, d):
    w = deque(string.replace(' ', ''))
    res = []

    while w:
        a = w.popleft()
        
        # Single left
        if not w:
            w.appendleft('x')
            w.appendleft(a)
            continue
        
        b = w.popleft()
        
        # Equal
        if a==b:
            w.appendleft(b)
            w.appendleft('x')
            w.appendleft(a)
            continue

        a_r,a_c = d[a]
        b_r,b_c = d[b]

        if a_r == b_r: # Same row
            res.append(key[a_r][(a_c+1)%5].upper())
            res.append(key[b_r][(b_c+1)%5].upper())
        elif a_c == b_c: # Same column
            res.append(key[(a_r+1)%5][a_c].upper())
            res.append(key[(b_r+1)%5][b_c].upper())
        else: # Different row and column
            res.append(key[a_r][b_c].upper())
            res.append(key[b_r][a_c].upper())

    return ''.join(res)

def main():
    key,d = create_key(input())
    print(encrypt(input(), key, d))

if __name__ == "__main__":
    main()