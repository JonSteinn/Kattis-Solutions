#ifndef _FENWICK_TREE_H
#define _FENWICK_TREE_H

// This Fenwick tree has indices [1..size], not [0..size-1]

#include <stdlib.h>

typedef unsigned long long ull;

typedef struct {
    ull *sums;
    int size;
} FenwickTree;

void fwt_update(FenwickTree *tree, int i, ull value) {
    while (i<=tree->size) {
        tree->sums[i] += value;
        i += i & -i;
    }
}

void fwt_increment(FenwickTree *tree, int i) {
    while (i<=tree->size) {
        tree->sums[i]++;
        i += i & -i;
    }
}

ull fwt_sum_to(FenwickTree *tree, int to) {
    ull s = 0;
    while (to > 0) {
        s += tree->sums[to];
        to -= to & (-to); 
    }
    return s;
}

ull fwt_sum_from(FenwickTree *tree, int from) {
    return fwt_sum_to(tree, tree->size) - fwt_sum_to(tree, from-1);
}

FenwickTree *fwt_create(int size) {
    FenwickTree* tree = (FenwickTree*)malloc(sizeof(FenwickTree));
    tree->sums = calloc(size+1, sizeof(ull));
    tree->size = size;
    return tree;
}

void fwt_destroy(FenwickTree* tree) {
    free(tree->sums);
    free(tree);
}

#endif
