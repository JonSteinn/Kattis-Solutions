from math import sqrt

def divisors(n):
    div = [] if n == 1 else [1]
    for i in range(2 if n%2 == 0 else 3,int(sqrt(n)+1),2):
        if n%i == 0:
            div.append(i)
            if i*2 != n:
                div.append(n//i)
    div.sort()
    return div

def is_multigram_of_length_n(string, n):
    seq = sorted(string[:n])
    for i in range(1,len(string)//n):
        if seq != sorted(string[i*n:(i+1)*n]):
            return False
    return True

def mutligram(string):
    div = divisors(len(string))
    for d in div:
        if is_multigram_of_length_n(string, d):
            return string[:d]
    return '-1'

def main():
    string = input()
    print(mutligram(string))

if __name__ == "__main__":
    main()