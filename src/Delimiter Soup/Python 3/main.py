def validate(code):
    stack = []
    opening = {'(', '[', '{'}
    closing = {')', ']', '}'}
    matches = {'(': ')', '[': ']', '{': '}'}
    for i, c in enumerate(code):
        if c in opening:
            stack.append(c)
        elif c in closing:
            if not stack or matches[stack.pop()] != c:
                return f'{c} {i}'
    return 'ok so far'

def main():
    input()
    print(validate(input()))

if __name__ == "__main__":
    main()