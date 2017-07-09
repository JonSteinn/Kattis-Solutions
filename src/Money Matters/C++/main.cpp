#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <unordered_map>
#include <unordered_set>

typedef std::unordered_map<int, std::vector<int>> edges;
typedef std::unordered_set<int> bag;

struct fast_stack
{
    int* mem;
    int* next;

    fast_stack(size_t max_cap)
    {
        mem = (int*)malloc(sizeof(int) *  max_cap);
        next = mem;
    }

    ~fast_stack()
    {
        free(mem);
    }

    bool is_empty()
    {
        return mem == next;
    }

    void push(int element)
    {
        *(next++) = element;
    }

    int pop()
    {
        return *(--next);
    }
};

bool possible(bag &remaining, edges &e, int *debts)
{
    while (remaining.size() > 0)
    {
        fast_stack open(10000000);
        open.push(*remaining.begin());
        int balance = 0;
        while (!open.is_empty())
        {
            int curr = open.pop();
            if (remaining.find(curr) == remaining.end()) continue;
            remaining.erase(curr);
            balance += debts[curr];
            std::vector<int> neighbors = e[curr];
            for (std::vector<int>::iterator it = neighbors.begin(); it != neighbors.end(); ++it)
            {
                if (remaining.find(*it) != remaining.end()) open.push(*it);
            }
        }
        if (balance) return false;
    }
    return true;
}

int main()
{
    int v, e;
    scanf("%d %d", &v, &e);
    size_t bucket_size = (size_t)(v / 0.75);
    bag remaining(bucket_size);
    edges m(bucket_size);
    int debts[v];
    for (int i = 0; i < v; i++)
    {
        scanf("%d", debts + i);
        remaining.insert(i);
    }
    for (int i = 0; i < e; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        m[a].push_back(b);
        m[b].push_back(a);
    }
    printf(possible(remaining, m, debts) ? "POSSIBLE\n" : "IMPOSSIBLE\n");
    return 0;
}