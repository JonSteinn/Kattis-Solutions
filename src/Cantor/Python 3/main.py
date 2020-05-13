def is_cantor(n,iterations=10):
    """
    At each iteration, split interval in three of equal length. If 
    n is in the open center one, it's not in the Cantor set. Otherwise,
    continue with the interval that n lands in.

    iterations=10 was just a guess. Can probably be a lot less, since
    we are reducing those intervals fast.
    """
    a, b = 0,1
    for _ in range(iterations):
        l = (b-a)/3
        c1,c2 = a + l, a + 2*l
        if n <= c1:
            b = c1
        elif n >= c2:
            a = c2
        else:
            return False
    return True

def main():
    while True:
        x = input()
        if x == 'END':
            break
        print('MEMBER' if is_cantor(float(x)) else 'NON-MEMBER')
    

if __name__ == "__main__":
    main()