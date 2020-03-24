def valid(word):
    return 'pink' in word or 'rose' in word

def main():
    s = sum(valid(input().lower()) for _ in range(int(input())))
    if s == 0:
        print('I must watch Star Wars with my daughter')
    else:
        print(s)

if __name__ == "__main__":
    main()