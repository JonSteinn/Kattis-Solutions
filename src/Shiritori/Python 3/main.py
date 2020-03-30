
def main():
    already_used, last = set(), ''
    for i in range(int(input())):
        curr = input()
        if last and (curr[0] != last[-1] or curr in already_used):
            print(f'Player {2 - (i+1)%2} lost')
            return
        else:
            last = curr
            already_used.add(curr)
    print('Fair Game')

if __name__ == "__main__":
    main()