def wword_rec(l,w,lis,mem):
    if l == 1:
        if 1 <= w <= 26:
            lis[-1] = chr(ord('a') + w - 1)
            return True
        else:
            return False
    
    if (l,w) in mem:
        return False
    
    for i in range(25,-1,-1):
        if wword_rec(l-1,w-i-1,lis,mem):
            lis[-l] = chr(ord('a')+i)
            return True
    
    mem.add((l,w))
    return False
        

def wword(l,w):
    lis = ['']*l
    memory = set()
    if wword_rec(l,w,lis,memory):
        return ''.join(lis)
    else:
        return 'impossible'

def main():
    print(wword(*map(int,input().split())))

if __name__ == "__main__":
    main()