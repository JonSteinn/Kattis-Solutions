
def m(n):
    # (2**63)**(1/9)=128 so we don't need to check that many m's. 
    # Can just bruteforce.
    for i in range(128,0,-1):
        z = i**9
        if z > n:
            continue
        if n % z == 0:
            return i
    return 1

def main():
    print(m(int(input()))) 

if __name__ == "__main__":
    main()