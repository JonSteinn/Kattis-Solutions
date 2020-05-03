def left(seq1,seq2):
    i = 0
    while i < len(seq1) and i < len(seq2) and seq1[i] == seq2[i]:
        i += 1
    return i

def right(seq1, seq2, l):
    i = len(seq1)-1
    j = len(seq2)-1
    while i > 0 and j > 0 and min(i,j) >= l and seq1[i] == seq2[j]:
        i -= 1
        j -= 1
    return j

def virus(seq1, seq2):
    l = left(seq1,seq2)
    r = right(seq1,seq2,l)
    if r < l:
        return 0
    else:
        return r-l+1

def main():
    print(virus(input(), input()))    

if __name__ == "__main__":
    main()