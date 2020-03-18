def is_valid(n,it):
    try:
        stack = [(next(it),True)]
        c,total = 0,0
        while c < n and stack:
            children, is_root = stack.pop()
            c += 1
            total += children
            if not is_root:
                children -= 1
            for _ in range(children):
                stack.append((next(it),False))
        return not bool(stack) and total == 2*(n-1)
    except StopIteration:
        return False

def main():
    print('YES' if is_valid(int(input()),map(int,input().split())) else 'NO')

if __name__ == "__main__":
    main()