def decode(msg):
    a = ord('a')-1
    lis = [0 if msg[0] == ' ' else ord(msg[0])-a]
    c_lis = [lis[0]]
    for i in range(1,len(msg)):
        lis.append(0 if msg[i] == ' ' else ord(msg[i])-a)
        while lis[i] < lis[i-1]:
            lis[i] += 27
        c_lis.append(lis[i]-lis[i-1])
    return ''.join(' ' if c == 0 else chr(c+a) for c in c_lis)

def encode(msg):
    a=ord('a')-1
    lis = [0 if msg[0] == ' ' else ord(msg[0])-a]
    for i in range(1,len(msg)):
        lis.append((lis[i-1] if msg[i] == ' ' else ord(msg[i])-a + lis[i-1]) % 27)
    return ''.join(' ' if c == 0 else chr(c+a) for c in lis)

def encrypt(s):
    t = []
    for c in s:
        a = 0
        if c != ' ':
            a = ord(c) - ord('a') + 1
        if len(t):
            t.append(t[-1] + a)
        else:
            t.append(a)

    u = []
    for c in t:
        c %= 27
        if c == 0:
            u.append(' ')
        else:
            u.append(chr(c + ord('a') - 1))
    return ''.join(u)

def decrypt(s):
    t = []
    tmp = 0
    for c in s:
        a = 0
        if c != ' ':
            a = ord(c) - ord('a') + 1
        a -= tmp
        while a < 0:
            a += 27
        tmp += a
        t.append(a)
    u = []
    for c in t:
        if c == 0:
            u.append(' ')
        else:
            u.append(chr(c + ord('a') - 1))
    return ''.join(u)

def test_case(cmd, txt):
    if cmd == 'e':
        print(encode(txt))
    else:
        print(decode(txt))

def main():
    for _ in range(int(input())):
        inp = input()
        test_case(inp[0], inp[2:])

if __name__ == "__main__":
    main()