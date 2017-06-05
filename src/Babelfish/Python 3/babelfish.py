import sys
from collections import defaultdict

dic = defaultdict(lambda: 'eh')
add = True
for line in sys.stdin:
    if add:
        if line == '\n':
            add = False
        else:
            s = line.split()
            dic[s[1]] = s[0]
    else:
        print(dic[line[0:-1]])