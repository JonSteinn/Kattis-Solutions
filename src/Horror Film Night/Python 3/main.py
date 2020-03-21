
def max_movies(a,b):
    curr_a,curr_b,dislikes_a,dislikes_b,counter = a.pop(), b.pop(), 0, 0, 0
    while True:
        if curr_a == curr_b:
            counter += 1
            if (not a and b) or (a and not b):
                return counter + 1
            if not a and not b:
                return counter
            curr_a,curr_b,dislikes_a,dislikes_b = a.pop(), b.pop(), 0, 0
        elif curr_a < curr_b:
            if dislikes_b == 1:
                if a:
                    curr_a = a.pop()
                else:
                    return counter + 1
            else:
                counter += 1
                if not a:
                    return counter + 1
                curr_a,dislikes_a,dislikes_b = a.pop(),0,dislikes_b+1
        else:
            if dislikes_a == 1:
                if b:
                    curr_b = b.pop()
                else:
                    return counter + 1
            else:
                counter += 1
                if not b:
                    return counter + 1
                curr_b,dislikes_b,dislikes_a = b.pop(),0,dislikes_a+1

def main():
    a = sorted(map(int, input().split()[1:]),reverse=True)
    b = sorted(map(int, input().split()[1:]),reverse=True)
    if not a:
        print(1 if b else 0)
    elif not b:
        print(1 if a else 0)
    else:
        print(max_movies(a,b))

if __name__ == "__main__":
    main()