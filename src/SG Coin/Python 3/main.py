def _H(prev, trans):
    for c in trans:
        prev = (prev*31+ord(c)) % 1000000007
    return prev

def find_hash(string, prev, hashes):
    for h in hashes:
        _h = _H(prev, string)
        token = h-7*_h
        while token < 0:
            token += 1000000007
        token %= 1000000007
        if token < 1000000000:
            print(string, token )
            return h

def main():
    hashes = {int(str(i)+'0'*7) for i in range(1,101)}
    prev = int(input())
    prev = find_hash('a', prev, hashes)
    hashes.remove(prev)
    find_hash('b', prev, hashes)

if __name__ == "__main__":
    main()