x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
print(max(((x1-x2)**2 + (y1-y2)**2)**0.5, ((x3-x4)**2 + (y3-y4)**2)**0.5))