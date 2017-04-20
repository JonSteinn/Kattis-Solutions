import sys

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "_": "..--",
    ".": "---.",
    ",": ".-.-",
    "?": "----"
}

back_morse = {}
for i in morse:
    back_morse[morse[i]] = i

for i in sys.stdin:
    len_lst = []
    translated = ""
    for c in i:
        if c == '\n':
            break
        m = morse[c]
        translated += m
        len_lst.append(len(m))
    len_lst.reverse()
    _next = 0
    s = ""
    for j in len_lst:
        s += back_morse[translated[_next:_next + j]]
        _next += j
    print(s)