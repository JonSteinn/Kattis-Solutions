#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int *p;
    int *used;
} UnionFind;

void uf_init(UnionFind* uf, int l) {
    uf->p = (int*)malloc(sizeof(int)*l);
    memset(uf->p, -1, l * sizeof(int));
    uf->used = (int*)calloc(l, sizeof(int));
}

void uf_destroy(UnionFind* uf) {
    free(uf->p);
    free(uf->used);
}

int uf_root(UnionFind *uf, int x) {
    while (uf->p[x] >= 0) {
        if (uf->p[uf->p[x]] >= 0) uf->p[x] = uf->p[uf->p[x]];
        x = uf->p[x];
    }
    return x;
}

int uf_connect(UnionFind *uf, int a, int b) {
    int ra = uf_root(uf, a), rb = uf_root(uf, b);
    if (ra - rb) {
        if (uf->p[ra] > uf->p[rb]) ra ^= rb ^= ra ^= rb;
        uf->p[ra] += uf->p[rb];
        uf->p[rb] = ra;
        uf->used[ra] += uf->used[rb];
    }
    
    if (uf->used[ra] < -uf->p[ra]) {
        uf->used[ra]++;
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int n,l,a,b;
    UnionFind uf;
    scanf("%d %d", &n, &l);
    uf_init(&uf,l);
    while (n--) {
        scanf("%d %d", &a, &b);
        printf(uf_connect(&uf, --a, --b) ? "LADICA\n" : "SMECE\n");
    }
    uf_destroy(&uf);
    return 0;
}