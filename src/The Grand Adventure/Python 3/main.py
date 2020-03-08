def can_finish(adventure):
    money_stack = []
    incense_stack = []
    gem_stack = []
    for c in adventure:
        if c == '$':
            money_stack.append(0)
        elif c == '|':
            incense_stack.append(0)
        elif c == '*':
            gem_stack.append(0)
        elif c == 't':
            if not incense_stack:
                return 'NO'
            else:
                incense_stack.pop()
        elif c == 'j':
            if not gem_stack:
                return 'NO'
            else:
                gem_stack.pop()
        elif c == 'b':
            if not money_stack:
                return 'NO'
            else:
                money_stack.pop()
    return 'NO' if money_stack or incense_stack or gem_stack else 'YES'

def main():
    for _ in range(int(input())):
        print(can_finish(input()))

if __name__ == "__main__":
    main()