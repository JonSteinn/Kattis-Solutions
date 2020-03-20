def get_line(n, word):
    if n > 2:
        return f'{n} bottles of {word} on the wall, {n} bottles of {word}.\nTake one down, pass it around, {n-1} bottles of {word} on the wall.'
    elif n == 2:
        return f'2 bottles of {word} on the wall, 2 bottles of {word}.\nTake one down, pass it around, 1 bottle of {word} on the wall.'
    else:
        return f'1 bottle of {word} on the wall, 1 bottle of {word}.\nTake it down, pass it around, no more bottles of {word}.'

n,w = int(input()),input()
print('\n\n'.join(get_line(i,w) for i in range(n,0,-1)))