def special(c):
    return 91 <= c <= 93 or 33 <= c <= 42

while True:
    try:
        n = int(input())
        print(" ".join(["".join(['\\' * ((1 << n)-1) + x if special(ord(x)) else x for x in string]) for string in input().split()]))
    except EOFError:
        break
