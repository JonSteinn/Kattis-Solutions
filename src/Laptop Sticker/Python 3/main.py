wc, hc, ws, hs = map(int, input().split())
print(int(min(wc-ws, hc-hs) >= 2))