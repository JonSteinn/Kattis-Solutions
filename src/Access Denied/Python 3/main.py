def get_time():    
    result = input()
    if result == "ACCESS GRANTED":
        return -1
    time = int(result.split("(")[-1][:-4])
    return time

def find_size():
    size = 1
    while True:
        print("A" * size)
        time = get_time()
        if time == -1:
            return None
        if time > 5:
            return size, time
        else:
            size += 1

def guess(n, t):
    pw = ["A"] * n
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    index_of_time = {(1+1+3+1+3)*i+1+3+10: i for i in range(21)}
    next_char_idx = 1
    t1 = t
    while True:
        pw[index_of_time[t1]] = alphabet[next_char_idx]
        print("".join(pw))
        t2 = get_time()
        if t2 == -1:
            break
        if t2 > t1:
            next_char_idx = 1
        else:
            next_char_idx += 1
        t1 = t2

def main():
    res = find_size()
    if res is not None:
        guess(*res)

if __name__ == "__main__":
    main()
