print(sum(1 if len(y) == 1 else int(y[1])-int(y[0])+1 for y in map(lambda x: x.split("-"), input().split(";"))))
    