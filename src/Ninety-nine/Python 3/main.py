def pick(n, alt):
    if n in (97, 98):
        k = 99 - n
    elif n % 3 == 0:
        # Loosing position
        # We start in one so a perfect opponent always wins
        # Something to counter his two versions of always picking the same
        k = 2 - int(alt)
    elif (n+1) % 3 == 0:
        k = 1
    else:
        k = 2
    return k

def main():
    n = 0
    my_turn = True
    alt = False
    while n < 99:
        if my_turn:
            n += pick(n, alt)
            print(n, flush=True)
            alt = not alt
        else:
            n = int(input())
        my_turn = not my_turn

if __name__ == "__main__":
    main()