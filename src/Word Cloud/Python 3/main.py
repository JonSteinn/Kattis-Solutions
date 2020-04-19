from math import ceil
from collections import deque

def cloud_height(max_w,words,most):
    total_h, line_w, line_h = 0, 0, 0
    while True:
        chars, cnt = words.popleft()
        pnt = 8 + ceil(40*(cnt-4)/(most-4))
        word_width = ceil(9/16 * chars * pnt)
        if line_w + word_width > max_w:
            total_h += line_h
            line_h = pnt
            line_w = word_width + 10
        else:
            line_h = max(pnt, line_h)
            line_w += word_width + 10

        if not words:
            total_h += line_h
            break
    return total_h

def main():
    cloud = 1
    while True:
        w,n = map(int,input().split())
        if w+n==0:
            break
        most, words = -1, deque()
        for _ in range(n):
            a,b = (lambda _a,_b: (_a,int(_b)))(*input().split())
            words.append((len(a),b))
            most = max(most, b)
        print(f'CLOUD {cloud}: {cloud_height(w,words,most)}')
        cloud += 1
        
if __name__ == "__main__":
    main()