def min_divisible_by(x):
    if x % 4 == 0:
        return 4
    if x % 6 == 0:
        return 6 if x<=18 else min(6,min_divisible_by(x//6))
    if x % 9 == 0:
        return 9 if x<=27 else min(9, min_divisible_by(x//9))
    if x % 2 == 0:
        return min(x//2, min_divisible_by(x//2))
    if x % 3 == 0:
        return min(x//3, min_divisible_by(x//3))
    for i in range(4,(int)(x**0.5)+1):
        if x % i == 0:
            return i
    return x

def foo1(x):
    if x == 3:
        return 4
    if x < 7:
        return 'No such base' 
    return min_divisible_by(x-3)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(foo1(n))

if __name__ == "__main__":
    main()