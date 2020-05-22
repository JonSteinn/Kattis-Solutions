def islands_of_length_n(lis, n):
    s=0
    for i in range(1,len(lis)-n):
        if max(lis[i-1],lis[i+n]) < min(lis[i:i+n]):
            s += 1
    return s

def islands(lis):
    return sum(islands_of_length_n(lis,n) for n in range(1,11))
        
def main():
    for i in range(int(input())):
        print(f'{i+1} {islands(list(map(int,input().split())))}')
    
if __name__ == "__main__":
    main()