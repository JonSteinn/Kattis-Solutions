#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct edge
{
    int v1, v2;
    double cost;
};

struct pos
{
    double x,y;
};

int comparator(const void* a, const void* b)
{
    double val = ((struct edge*)a)->cost - ((struct edge*)b)->cost;
    return val < 0 ? -1 : val > 0 ? 1 : 0;
}

int find(int x, int* parents)
{
    if (parents[x] == x) return x;
    parents[x] = find(parents[x], parents);
    return parents[x];
}

void join(int x, int y, int* parents)
{
    parents[find(x, parents)] = find(y, parents);
}

int connected(int x, int y, int* parents)
{
    return find(x, parents) == find(y, parents);
}

void test_case()
{
    int v;
    scanf("%d",&v);
    struct pos vertices[v];
    for (int i = 0; i < v; i++) scanf("%lf %lf", &vertices[i].x, &vertices[i].y);
    int e = (v * (v-1)) >> 1;;
    struct edge edges[e];
    int index = 0;
    for (int i = 0; i < v; i++)
    {
        for (int j = i + 1; j < v; j++)
        {
            edges[index].v1 = i;
            edges[index].v2 = j;
            double dx = vertices[i].x - vertices[j].x;
            double dy = vertices[i].y - vertices[j].y;
            edges[index++].cost = dx * dx + dy * dy;
        }
    }

    int parents[v];
    for (int i = 0; i < v; i++) parents[i] = i;

    qsort(edges, (size_t)e, sizeof(struct edge), comparator);
    int marked = 0;
    index = 0;
    double dist_sum = 0.0;
    while (marked < v - 1)
    {
        if (!connected(edges[index].v1, edges[index].v2, parents))
        {
            dist_sum += sqrt(edges[index].cost);
            join(edges[index].v1, edges[index].v2, parents);
            marked++;
        }
        index++;
    }
    printf("%.6lf\n", dist_sum);
}

int main()
{
    int test_cases;
    scanf("%d",&test_cases);
    while (test_cases--) test_case();
    return 0;
}