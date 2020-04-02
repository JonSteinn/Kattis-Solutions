from collections import Counter

def main():
    party = dict((input().rstrip(), input().rstrip()) for _ in range(int(input())))
    votes = Counter(input().rstrip() for _ in range(int(input())))
    top2 = votes.most_common(2)
    if len(top2) == 1:
        print(party[top2[0][0]])
    elif top2[0][1] == top2[1][1]:
        print('tie')
    else:
        print(party[top2[0][0] if top2[0][1] > top2[1][1] else top2[1][0]])

if __name__ == "__main__":
    main()
