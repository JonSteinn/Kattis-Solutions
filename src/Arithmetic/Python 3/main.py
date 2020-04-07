from collections import deque

def main():
    binary = ['000','001','010','011','100','101','110','111']
    hexidecimal = deque()
    waiting = deque()
    for c in reversed(input()):
        for i in reversed(binary[ord(c)-48]):
            waiting.appendleft(i)
        if len(waiting) >= 4:
            s = sum((waiting.pop() == '1') << i for i in range(4))
            if s < 10:
                hexidecimal.appendleft(str(s))
            else: 
                hexidecimal.appendleft(chr(65 + (s-10)))
    if waiting:
        s = sum((waiting.pop() == '1') << i for i in range(len(waiting)))
        if s < 10:
            hexidecimal.appendleft(str(s))
        else: 
            hexidecimal.appendleft(chr(65 + (s-10)))
    while len(hexidecimal) > 1 and hexidecimal[0] == '0':
        hexidecimal.popleft()
    print(''.join(hexidecimal))

if __name__ == "__main__":
    main()