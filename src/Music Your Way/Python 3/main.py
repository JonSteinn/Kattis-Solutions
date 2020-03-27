from collections import namedtuple

def main():
    fields = input().split()
    Tune = namedtuple('Tune', fields)
    tunes = [Tune(*input().split()) for _ in range(int(input()))]
    first = True
    for _ in range(int(input())):
        if not first:
            print()
        else:
            first = False
        sort_by = input()
        tunes.sort(key=lambda z: getattr(z,sort_by))
        print(*fields)
        print('\n'.join(' '.join(tune) for tune in tunes))

if __name__ == "__main__":
    main()