MOD = 10000
TARGET = 'welcome to code jam'
TARGET_LEN = 19

def dp(i, j, sentence, mem):
    #Starting from i in sentence, how many subwords "welcome to code jam"[j:] are in the remaining

    if len(sentence) - i < TARGET_LEN - j:
        return 0
    
    if mem[i][j] == -1:
        if j == 18:
            mem[i][j] = sentence[i:].count(TARGET[-1])
        else:
            mem[i][j] = ((dp(i+1,j+1,sentence,mem) if sentence[i] == TARGET[j] else 0) + dp(i+1,j,sentence,mem)) % MOD
    return mem[i][j]

def occurrences(sentence):
    mem = [[-1]*19 for _ in range(len(sentence))]
    cnt = str(dp(0,0,sentence,mem))
    return f"{(4-len(cnt))*'0'}{cnt}"

def main():
    print("\n".join(f'Case #{i+1}: {occurrences(sentence)}' for i,sentence in enumerate(input() for _ in range(int(input())))))

if __name__ == "__main__":
    main()
