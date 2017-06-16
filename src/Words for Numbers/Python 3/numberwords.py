import sys

lo = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

hi = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}


def to_words(n):
    if n < 20:
        return lo[n]
    if n % 10 == 0:
        return hi[n // 10]
    return "-".join([hi[n // 10], lo[n % 10]])


for line in sys.stdin:
    s = " ".join([word if not word.isdigit() else to_words(int(word)) for word in line.split()])
    print(s[0].upper() + s[1:])