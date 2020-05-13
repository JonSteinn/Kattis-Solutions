class Key:
    def __init__(self, x, s, p):
        self.x = x
        self.p = p
        self.s_i = {c:i for i,c in enumerate(s)}

    def decode(self, c):
        n = len(c)
        d = int(n**1.5 + self.x) % n
        m = ['#']*n
        m[d] = self.p[self.s_i[c[d]]]

        d_more, d_less = d, (d-1+n)%n
        while d_less != d:
            m[d_less] = self.p[self.s_i[c[d_less]] ^ self.s_i[m[d_more]]]
            d_less, d_more = (d_less-1+n)%n, (d_more-1+n)%n

        return ''.join(m)

def main():
    while True:
        x = int(input())
        if x == 0:
            break
        print(Key(x, input(), input()).decode(input()))

if __name__ == "__main__":
    main()