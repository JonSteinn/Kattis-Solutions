from collections import defaultdict

def get_input():
    input()
    translations = [defaultdict(list), defaultdict(list)]
    sentence = input().split()
    for _ in range(int(input())):
        d,e,s = input().split()
        translations[s[0]=='c'][d].append(e)
    return sentence, translations

def number_of_correct_and_incorrect(sentence, translations):
    total, correct = 1, 1
    for word in sentence:
        corr = len(translations[True][word])
        tot = corr + len(translations[False][word])
        correct *= corr
        total *= tot
    return correct, total-correct

def print_only_translation(sentence, translations, is_correct):
    if is_correct:
        print(f"{' '.join(translations[True][word][0] for word in sentence)}\ncorrect")
    else:
        print(f"{' '.join(translations[True][word][0] if translations[True][word] else translations[False][word][0] for word in sentence)}\nincorrect")

def main():
    sentence, translations = get_input()
    correct, incorrect = number_of_correct_and_incorrect(sentence,translations)
    if correct + incorrect == 1:
        print_only_translation(sentence, translations, correct == 1)
    else:
        print(f'{correct} correct\n{incorrect} incorrect')

if __name__ == "__main__":
    main()
