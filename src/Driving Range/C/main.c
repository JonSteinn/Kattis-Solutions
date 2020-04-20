#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int u,v,w;
} edge;

int edge_comparator(const void *e1, const void *e2) { 
    return ((edge*)e1)->w - ((edge*)e2)->w; 
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

int kruskal(int v, int e, edge *edges) {
    qsort(edges, e, sizeof(edge), edge_comparator);
    int uf[1000001] = {[0 ... 1000000] = -1};

    int gathered = 0, last = 0;
    for (int i = 0; i < e && gathered < v-1; i++) {
        if (!connect(uf, edges[i].u, edges[i].v)) continue;
        last = edges[i].w;
        gathered++;
    }

    return gathered == v-1 ? last : -1;
}

int main(void) {
    int v,e;
    scanf("%d %d", &v, &e);

    edge edges[e];
    for (int i = 0; i < e; i++) scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].w);

    int last;
    if (e < v-1 || (last = kruskal(v,e,edges)) < 0) printf("IMPOSSIBLE\n");
    else printf("%d\n", last);

    return 0;
}
