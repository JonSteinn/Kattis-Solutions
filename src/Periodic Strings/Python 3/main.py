from textwrap import wrap

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

def min_permutation_repeat(n,s):
    if s.count(s[0]) == n:
        return 1
    if n in primes:
        return n
    for i in range(2,n):
        if n % i == 0 and (lambda w: all(w[i+1] == w[i][-1] + w[i][:-1] for i in range(0,n//i - 1)))(wrap(s,i)):
            return i
    return n
                
def main():
    w = input()
    print(min_permutation_repeat(len(w),w))
    
if __name__ == "__main__":
    main()
