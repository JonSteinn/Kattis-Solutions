import sys

factorials = {0: 1}
for i in range(1, 101):
    factorials[i] = i * factorials[i - 1]

for _input in sys.stdin:
    word = str(_input.split()[0])
    occurrences = {}
    for char in word:
        if ord(char) in occurrences:
            occurrences[ord(char)] += 1
        else:
            occurrences[ord(char)] = 1
    value = factorials[len(word)]
    for i in occurrences:
        value = value // factorials[occurrences[i]]
    print(value)