#include <stdio.h>

struct vertex
{
    int x, y;
};

int det(struct vertex* v1, struct vertex* v2)
{
    return v1->x * v2->y - v1->y * v2->x;
}

void find_area(struct vertex* vertices, int v)
{
    int sum = 0;
    for (int i = 0; i < v - 1; i++) sum += det(vertices + i, vertices + i + 1);
    sum += det(vertices + v - 1, vertices);
    if (sum & 1) printf("%.1f\n", sum / 2.0);
    else printf("%d\n", sum >> 1);
}

void read_vertices(struct vertex* vertices, int v)
{
    for (int i = 0; i < v; i++) scanf("%d %d", &(vertices + i)->x, &(vertices + i)->y);
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int v;
        scanf("%d",&v);
        struct vertex vertices[v];
        read_vertices(vertices, v);
        find_area(vertices, v);
    }
    return 0;
}