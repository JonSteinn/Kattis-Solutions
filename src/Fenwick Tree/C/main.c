#include <stdio.h>
#include <stdlib.h>

typedef struct {
    long long* sums;
    int size;
} FenwickTree;

void update(FenwickTree* tree, int i, int value) {
    while (i<=tree->size) {
        tree->sums[i] += value;
        i += i & -i;
    }
}

long long sum(FenwickTree* tree, int i) {
    long long s = 0;
    while (i > 0) {
        s += tree->sums[i];
        i -= i & (-i); 
    }
    return s;
}

FenwickTree* create(int size) {
    FenwickTree* tree = (FenwickTree*)malloc(sizeof(FenwickTree));
    tree->sums = calloc(size+1, sizeof(long long));
    tree->size = size;
    return tree;
}

void destroy(FenwickTree* tree) {
    free(tree->sums);
    free(tree);
}

int main() {
    int n,q,i,v;
    char c;
    scanf("%d %d",&n,&q);
    FenwickTree* tree = create(n);
    while(q--) {
        scanf(" %c", &c);
        if (c == '+') {
            scanf("%d %d", &i, &v);
            update(tree, i+1, v);
        } else {
            scanf("%d", &i);
            if (i) {
                printf("%lld\n", sum(tree,i));
            } else {
                printf("0\n");
            }
        }
    }
    destroy(tree);
    return 0;
}