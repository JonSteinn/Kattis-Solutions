def main():
    n,p,m = map(int,input().split())
    counter = {input(): 0 for _ in range(n)}
    winners = []
    for _ in range(m):
        name, score = input().split()
        if counter[name] == -1:
            continue
        counter[name] += int(score)
        if counter[name] >= p:
            winners.append(name)
            counter[name] = -1
    if not winners:
        print('No winner!')
    else:
        print('\n'.join((f'{name} wins!' for name in winners)))

if __name__ == "__main__":
    main()