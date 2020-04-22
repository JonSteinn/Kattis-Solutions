from collections import defaultdict, Counter

def main():
    word_counter = Counter()
    user_words = defaultdict(set)
    for _ in range(int(input())):
        name, *words = input().split()
        for word in words:
            user_words[name].add(word)
            word_counter[word] += 1
    shared = set.intersection(*user_words.values())
    if shared:
        print('\n'.join(sorted(shared, key=lambda z: (-word_counter[z],z))))
    else:
        print('ALL CLEAR')

if __name__ == "__main__":
    main()