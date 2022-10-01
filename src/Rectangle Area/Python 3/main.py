x1, y1, x2, y2 = map(float, input().split())
area = abs(x1 - x2) * abs(y1 - y2)
print(f"{area:.3f}")