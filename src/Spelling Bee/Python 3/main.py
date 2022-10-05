original = input()
for _ in range(int(input())):
    word = input()
    word_set = set(word)
    if len(word) > 3 and not word_set.difference(original) and original[0] in word_set:
        print(word)