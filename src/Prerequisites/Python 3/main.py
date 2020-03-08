def is_satisfied(selected, c_courses, r):
    for course in c_courses:
        if course in selected:
            r -= 1
            if r <= 0:
                return True
    return r <= 0

def test_case(k,m):
    selected = set(map(int, input().split()))
    valid = True
    for _ in range(m):
        if not valid:
            input()
            continue
        r, c_courses = (lambda z: (z[1], z[2:]))(list(map(int, input().split())))
        if not is_satisfied(selected, c_courses, r):
            valid = False
    print('yes' if valid else 'no')

def main():
    while True:
        x = input().split()
        if len(x) == 1:
            break
        test_case(int(x[0]), int(x[1]))


if __name__ == "__main__":
    main()