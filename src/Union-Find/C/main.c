#include <stdio.h>
#include <stdlib.h>

/* I did learn this from the Sedgewick&Wayne book so... well... uhh... just gonna do that */

int* parent;
int* size;

int uf_find(int p)
{
    int root = p;
    while (root != parent[root]) root = parent[root];
    while (p != root)
    {
        int _p = parent[p];
        parent[p] = root;
        p = _p;
    }
    return root;
}

int uf_connected(int p, int q)
{
    return uf_find(p) == uf_find(q);
}

void uf_union(int p, int q)
{
    int root_p = uf_find(p), root_q = uf_find(q);
    if (root_p != root_q)
    {
        if (size[root_p] < size[root_q])
        {
            parent[root_p] = root_q;
            size[root_q] += size[root_p];
        }
        else
        {
            parent[root_q] = root_p;
            size[root_p] += size[root_q];
        }
    }
}

int main()
{
    int len, queries;
    scanf("%d %d", &len, &queries);

    if (queries)
    {
        size = (int*)malloc((size_t)(len << 3));
        parent = size + len;

        int i;
        for (i = 0; i < len; i++)
        {
            size[i] = 1;
            parent[i] = i;
        }

        char operator;
        int p, q;
        while (queries-- > 0)
        {
            scanf(" %c %d %d", &operator, &p, &q);
            if (operator == '=') uf_union(p, q);
            else printf(uf_connected(p, q) ? "yes\n" : "no\n");
        }
    }
    free(size);
    return 0;
}