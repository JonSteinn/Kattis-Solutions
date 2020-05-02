#include <stdio.h>
#include <stdlib.h> 
#include <string.h>

typedef struct {
    int x,y,z;
    int index;
} Point3d;

typedef struct {
    int from, to;
    int weight;
} Edge;

int x_comp(const void *lhs, const void *rhs) {
    return ((Point3d*)lhs)->x - ((Point3d*)rhs)->x;
}

int y_comp(const void *lhs, const void *rhs) {
    return ((Point3d*)lhs)->y - ((Point3d*)rhs)->y;
}

int z_comp(const void *lhs, const void *rhs) {
    return ((Point3d*)lhs)->z - ((Point3d*)rhs)->z;
}

int edge_comp(const void *lhs, const void *rhs) {
    return ((Edge*)lhs)->weight - ((Edge*)rhs)->weight;
}

void find_edges(Point3d *planets, int n, Edge *edges, int e) {
    qsort((void*)planets, n, sizeof(Point3d), x_comp);
    for (int i = 0; i < n-1; i++) {
        edges[i] = (Edge){
            .from = planets[i].index,
            .to = planets[i+1].index,
            .weight = abs(planets[i].x - planets[i+1].x)
        };
    }

    int offset = n-1;
    qsort((void*)planets, n, sizeof(Point3d), y_comp);
    for (int i = 0; i < n-1; i++) {
        edges[offset+i] = (Edge){
            .from = planets[i].index,
            .to = planets[i+1].index,
            .weight = abs(planets[i].y - planets[i+1].y)
        };
    }

    offset *= 2;
    qsort((void*)planets, n, sizeof(Point3d), z_comp);
    for (int i = 0; i < n-1; i++) {
        edges[offset+i] = (Edge){
            .from = planets[i].index,
            .to = planets[i+1].index,
            .weight = abs(planets[i].z - planets[i+1].z)
        };
    }

    qsort(edges, e, sizeof(Edge), edge_comp);
}

int uf_find(int* p, int a) {
    while (p[a] >= 0) {
        if (p[p[a]] >= 0) p[a] = p[p[a]];
        a = p[a];
    }
    return a;
}

int connect(int* p, int a, int b) {
    int rA = uf_find(p,a), rB = uf_find(p, b);
    if (rA == rB) return 0;
    if (p[rA] > p[rB]) rA ^= rB ^= rA ^= rB;
    p[rA] += p[rB];
    p[rB] = rA;
    return 1;
}

int main(void) {
    int n;
    scanf("%d", &n);
    Point3d planets[n];
    for (int i = 0; i < n; i++) {
        scanf("%d %d %d", &planets[i].x, &planets[i].y, &planets[i].z);
        planets[i].index = i;
    }
    
    int e = 3*(n-1);
    Edge edges[e];
    find_edges(planets, n, edges, e);

    int uf[n];
    memset(uf, -1, sizeof(int)*n);

    int included = 0;
    unsigned long long total = 0;
    for (int i = 0; i < e && included < n-1; i++) {
        if (!connect(uf, edges[i].from, edges[i].to)) continue;
        total += edges[i].weight;
        included++;
    }

    printf("%llu\n", total);

    return 0;
}