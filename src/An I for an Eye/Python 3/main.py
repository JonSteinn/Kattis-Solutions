rules = {
    2: {
        'at': '@',
        'to': '2',
        'be': 'b',
        'oh': 'o',

        'At': '@',
        'To': '2',
        'Be': 'B',
        'Oh': 'O'
    },
    3: {
        'and': '&',
        'one': '1',
        'won': '1',
        'too': '2',
        'two': '2',
        'for': '4',
        'bea': 'b',
        'bee': 'b',
        'sea': 'c',
        'see': 'c',
        'eye': 'i',
        'owe': 'o',
        'are': 'r',
        'you': 'u',
        'why': 'y',
        
        'And': '&',
        'One': '1',
        'Won': '1',
        'Too': '2',
        'Two': '2',
        'For': '4',
        'Bea': 'B',
        'Bee': 'B',
        'Sea': 'C',
        'See': 'C',
        'Eye': 'I',
        'Owe': 'O',
        'Are': 'R',
        'You': 'U',
        'Why': 'Y'
    },
    4: {
        'four': '4',

        'Four': '4'
    }
}

def update(string):
    lis = list(string)
    l = len(lis)
    curr = 0
    while curr < l - 1:
        if curr < l - 3 and string[curr:curr+4] in rules[4]:
            lis[curr] = rules[4][string[curr:curr+4]]
            lis[curr+1] = '\0'
            lis[curr+2] = '\0'
            lis[curr+3] = '\0'
            curr += 4
        elif curr < l - 2 and string[curr:curr+3] in rules[3]:
            lis[curr] = rules[3][string[curr:curr+3]]
            lis[curr+1] = '\0'
            lis[curr+2] = '\0'
            curr += 3
        elif string[curr:curr+2] in rules[2]:
            lis[curr] = rules[2][string[curr:curr+2]]
            lis[curr+1] = '\0'
            curr += 2
        else:
            curr += 1

    return ''.join((c for c in lis if c != '\0'))

def main():
    for _ in range(int(input())):
        print(' '.join((update(string) for string in input().split())))

if __name__ == "__main__":
    main()