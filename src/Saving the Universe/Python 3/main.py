def find_next(engines, words, used):
    remaining = len(engines)-1
    for word in words:
        if engines[word] != used:
            if remaining == 1:
                return True
            engines[word] = used
            remaining -= 1
    return False

def swaps_required(engines, words):
    swaps, used = 0, True
    for w in words:
        engines[w] = True
        break
    while find_next(engines, words, used):
        swaps, used = swaps + 1, not used
    return swaps

def main():
    for case in range(int(input())):
        engines = {input(): False for _ in range(int(input()))}
        word_gen = (input() for _ in range(int(input())))
        print(f'Case #{case+1}: {swaps_required(engines, word_gen)}')

if __name__ == "__main__":
    main()