#include <iostream>
#include <vector>
#include <unordered_map>

// UF from https://github.com/SuprDewd/CompetitiveProgramming/blob/master/code/data-structures/union_find.cpp
struct union_find {
    std::vector<int> p;

    union_find(int n) : p(n, -1) { }

    int find(int x) {
        return p[x] < 0 ? x : p[x] = find(p[x]);
    }

    void unite(int x, int y) {
        int xp = find(x), yp = find(y);
        if (xp != yp) {
            if (p[xp] > p[yp]) xp ^= yp ^= xp ^= yp;
            p[xp] += p[yp];
            p[yp] = xp;
        }
    }

    int size(int x) {
        return -p[find(x)];
    }
};

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;
    while(n--)
    {
        int f;
        std::cin >> f;

        union_find uf(f << 1);
        std::unordered_map<std::string, int> id((size_t)((f << 1) / 0.7));
        int next_id = 0;

        for (int i = 0; i < f; i++) {
            std::string a, b;
            std::cin >> a >> b;
            if (id.find(a) == id.end()) id[a] = next_id++;
            if (id.find(b) == id.end()) id[b] = next_id++;

            uf.unite(id[a], id[b]);
            std::cout << uf.size(id[a]) << '\n';
        }
    }
    return 0;
}