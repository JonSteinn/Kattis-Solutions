from collections import Counter

def main():
    print(((lambda w,l: Counter((w[0:l],w[l:l<<1],w[l<<1:])))(*(lambda i: (i,len(i)//3))(input()))).most_common(1)[0][0])

if __name__ == "__main__":
    main()