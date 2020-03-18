from sys import stdin as lines

def main():
    for line in lines:
        i,j,l = 0,0, len(line)-1
        while i < l-1:
            if line[i] == '0' and (line[i+1] == 'x' or line[i+1] == 'X'):
                j = i+2
                while j < l and ('a' <= line[j] <= 'f' or 'A' <= line[j] <= 'F' or '0' <= line[j] <= '9'):
                    j += 1
                if j != i+2:
                    b16 = line[i:j]
                    print(f'{b16} {int(b16, base=16)}')
                i = j
            else:
                i += 1

if __name__ == "__main__":
    main()