from collections import defaultdict

def get_types_dict(s1):
    types = defaultdict(lambda: 0, {s1: 1})
    for i in range(len(s1)):
        types[s1[0:i] + s1[i+1:]] = 2
    for i in range(len(s1)+1):
        types[s1[0:i] + 'A' + s1[i:]] = 3
        types[s1[0:i] + 'C' + s1[i:]] = 3
        types[s1[0:i] + 'G' + s1[i:]] = 3
        types[s1[0:i] + 'T' + s1[i:]] = 3
    return types

def get_types_count(s2, d):
    counter = [0]*4
    for i in range(len(s2)):
        for j in range(i+1,len(s2)+1):
            counter[d[s2[i:j]]] += 1
    return counter

def find_types(s1,s2):
    types = get_types_dict(s1)
    counter = get_types_count(s2, types)
    return counter[1:]

def main():
    while True:
        inp = input()
        if inp == '0':
            break
        print(*find_types(*inp.split()))

if __name__ == "__main__":
    main()