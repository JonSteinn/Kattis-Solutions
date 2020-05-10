def solve(l1,a1,l2,a2,lt,at):
    det = (a2*l1 - a1*l2)
    if det != 0:
        x = a2*lt - at*l2
        y = at*l1 - a1*lt
        x, rx = divmod(x,det)
        y, ry = divmod(y,det)
        if rx == ry == 0 and x > 0 and y > 0:
            return (x,y)
    elif l1*at == a1*lt and lt*a2 == at*l2:
        sol = ('?',)
        for x in range(1, min(lt//l1 if lt%l1 == 0 else lt//l1 + 1, at//a1 if at % a1 == 0 else at//a1+1)):
            if (lt-x*l1) % l2 == 0 and (at-x*a1) % a2 == 0:
                y = (at-x*a1)//a2
                if y > 0:
                    if sol != ('?',):
                        return ('?')
                    sol = (x,y)
                else:
                    break
        return sol
    return ('?',)

def main():
    for _ in range(int(input())):
        print(*solve(*map(int,input().split())))
    
if __name__ == "__main__":
    main()