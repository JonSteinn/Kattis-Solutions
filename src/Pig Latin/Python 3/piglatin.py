import sys

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}


def pig_lat(string):
    if string[0] not in vowels:
        for i, c in enumerate(string):
            if c in vowels:
                return string[i:] + string[:i] + 'ay'
    else:
        return string + 'yay'


for line in sys.stdin:
    print(" ".join(map(pig_lat, line.split())))