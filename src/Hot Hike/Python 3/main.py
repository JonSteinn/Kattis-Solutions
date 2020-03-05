def find(n, temps):
    m_i, m_t = (-1,41)
    for i in range(n-2):
        m = max(temps[i],temps[i+2])
        if m < m_t:
            m_t = m
            m_i = i
    return m_i + 1, m_t

def main():
    print("%d %d" % find(int(input()), list(map(int, input().split()))))

if __name__ == "__main__":
    main()
