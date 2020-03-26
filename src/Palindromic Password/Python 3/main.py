from itertools import islice

all_palindrome = set()

def next_palindrome(word):
    best,best_w,num = 10000000000, 0, int(word)
    for p in all_palindrome:
        dist = abs(p-num)
        if dist < best:
            best = dist
            best_w = p
    w = str(best_w)
    if len(w) == 5:
        w = '0' + w
    return w

def generate_palindromes():
    s = '0123456789'
    for a in islice(s,1,None):
        for b in s:
            for c in s:
                all_palindrome.add(int(f'{a}{b}{c}{c}{b}{a}'))

def main():
    generate_palindromes()
    for _ in range(int(input())):
        print(next_palindrome(input()))

if __name__ == "__main__":
    main()