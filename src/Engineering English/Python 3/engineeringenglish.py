import sys

d = set()
for line in sys.stdin:
    out_line = []
    for word in line.split():
        if word.upper() in d:
            out_line += ['.']
        else:
            d.add(word.upper())
            out_line += [word]
    print(" ".join(out_line))