from itertools import islice

def main():
    n,k = map(int,input().split())
    pokemons = [tuple(map(int,input().split())) for _ in range(n)]
    collected = set()
    for j in range(3):
        for i,_ in islice(sorted(enumerate(pokemons), key=lambda z: z[1][j], reverse=True),0,k):
            collected.add(i)
    print(len(collected))

if __name__ == "__main__":
    main()