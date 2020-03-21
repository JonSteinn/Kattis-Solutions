from collections import defaultdict

def generate_maps(hard):
    ends = ['a','o','u']
    d1 = defaultdict(lambda: [None, 1000])
    d2 = defaultdict(lambda: [None, 1000])
    s_hard = sorted(hard)
    for i in range(97,97+26):
        for x in s_hard:
            dist = abs(i-ord(x))
            if dist < d1[chr(i)][1]:
                d1[chr(i)][0] = x
                d1[chr(i-32)][0] = chr(ord(x)-32)
                d1[chr(i)][1] = dist
        for x in ends:
            dist = abs(i-ord(x))
            if dist < d2[chr(i)][1]:
                d2[chr(i)][0] = f'{x}h'
                d2[chr(i)][1] = dist
                d2[chr(i-32)][0] = f'{x}h'
                d2[chr(i-32)][1] = 0
    return dict(d1),dict(d2)

def extend_hards(hard):
    return hard.union({chr(ord(c)-32) for c in hard})

def nimionesify_single(word,h_map,end,hard):
    word_lis = list(word)
    word_lis[0] = h_map[word_lis[0]][0]
    replacement = word_lis[0] if ord(word_lis[0]) >= 97 else chr(ord(word_lis[0])+32)
    after_first = False
    for i,c in enumerate(word_lis):
        if i==0:
            continue
        if c in hard and after_first:
            word_lis[i] = replacement
        if c == '-':
            after_first = True
            word_lis[i] = ''
    if word_lis[-1] in hard:
        return f'{"".join(word_lis)}{end[word_lis[-1]][0]}'
    else:
        return ''.join(word_lis)

def nimionesify(words,h_map,end,hard):
    hard = extend_hards(hard)
    return ' '.join(nimionesify_single(word,h_map,end,hard) for word in words)

def main():
    hard = {'b', 'c', 'd', 'g', 'k', 'n', 'p', 't'}
    h_map,end = generate_maps(hard)
    words = input().split()
    print(nimionesify(words,h_map,end,hard))

if __name__ == "__main__":
    main()