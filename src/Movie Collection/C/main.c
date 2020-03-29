#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int* sums;
    int size;
} FenwickTree;

void update(FenwickTree* tree, int i, int value) {
    while (i<=tree->size) {
        tree->sums[i] += value;
        i += i & -i;
    }
}

int sum(FenwickTree* tree, int i) {
    int s = 0;
    while (i > 0) {
        s += tree->sums[i];
        i -= i & (-i); 
    }
    return s;
}

FenwickTree* create(int r, int m) {
    int size = r+m;
    FenwickTree* tree = (FenwickTree*)malloc(sizeof(FenwickTree));
    tree->sums = calloc(size+1, sizeof(int));
    tree->size = size;
    for (int i = 0; i < r; i++) update(tree, i+1, 0);
    for (int i = r; i < size; i++) update(tree, i+1, 1);
    return tree;
}

void destroy(FenwickTree* tree) {
    free(tree->sums);
    free(tree);
}

void test_case(int m, int r, int* arr) {
    FenwickTree* tree = create(r,m);
    int index_tracker[m+1];
    for (int i = 1; i <= m; i++) index_tracker[i] = r+i;
    int first = 1;
    for (int i = 0; i < r; i++) {
        if (first) first = 0;
        else putchar(' ');
        printf("%d", sum(tree, index_tracker[arr[i]])-1);
        update(tree, index_tracker[arr[i]], -1);
        index_tracker[arr[i]] = r - i;
        update(tree, index_tracker[arr[i]], 1);
    }
    putchar('\n');
    destroy(tree);
}

int main() {
    int n;
    scanf("%d",&n);
    while(n--) {
        int m,r;
        scanf("%d %d", &m, &r);
        int arr[r];
        for (int i = 0; i < r; i++) scanf("%d", arr + i);
        test_case(m,r,arr);
    }
    return 0;
}