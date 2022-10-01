upper_right, lower_right = ({f"{i}{s}" for i in range(1, 9)} for s in ("-","+"))
upper_left, lower_left = ({f"{s}{i}" for i in range(1, 9)} for s in ("-","+"))
rotten_left, rotten_right = False, False
for _ in range(int(input())):
    tooth, state = input().split()
    if state == "m":
        upper_left.discard(tooth)
        lower_left.discard(tooth)
        upper_right.discard(tooth)
        lower_right.discard(tooth)
    elif tooth in upper_left or tooth in lower_left:
        rotten_left = True
    else:
        rotten_right = True


if min(map(len, (upper_left, lower_left))) > 0 and not rotten_left:
    print(0)
elif min(map(len, (upper_right, lower_right))) > 0 and not rotten_right:
    print(1)
else:
    print(2)
