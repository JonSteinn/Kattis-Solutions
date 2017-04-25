#include <cstdio>
#include <vector>

// From T-414-AFLV (Minor modifications)
struct union_find
{
    std::vector<int> parent;
    union_find(size_t n)
    {
        parent = std::vector<int>(n);
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int x)
    {
        if (parent[x] == x) return x;
        parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y)
    {
        parent[find(x)] = find(y);
    }
    bool connected(int x, int y)
    {
        return find(x) == find(y);
    }
};

int main()
{
    size_t houses, connections;
    scanf("%zu %zu", &houses, &connections);
    union_find uf(houses);
    for (int i = 0; i < connections; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        uf.unite(a - 1, b - 1);
    }
    bool connected = true;
    for (int i = 1; i < houses; i++)
    {
        if (!uf.connected(0, i))
        {
            printf("%d\n", i + 1);
            connected = false;
        }
    }
    if (connected) printf("Connected\n");
    return 0;
}