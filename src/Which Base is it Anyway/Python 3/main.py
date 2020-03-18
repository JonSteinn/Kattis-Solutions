def to_oct(string):
    try:
        return int(string, base=8)
    except ValueError:
        return 0

def convert_all(n_str):
    return to_oct(n_str), int(n_str), int(n_str,base=16)

def main():
    for _ in range(int(input())):
        a,b = input().split()
        print(a,*convert_all(b))
    

if __name__ == "__main__":
    main()