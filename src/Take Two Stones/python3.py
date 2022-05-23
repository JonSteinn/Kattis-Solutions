stones_left = int(input())
if stones_left % 2 == 1:
    print('Alice')
elif stones_left % 2 == 0:
    print('Bob')
else:
    print('IDK what you entered, but it broke my logic. :( ')
