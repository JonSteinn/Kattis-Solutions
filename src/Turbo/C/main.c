#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *sums;
    int size;
} FenwickTree;

void fwt_decrement(FenwickTree *tree, int i) {
    while (i<=tree->size) {
        tree->sums[i]--;
        i += i & -i;
    }
}

void fwt_increment(FenwickTree *tree, int i) {
    while (i<=tree->size) {
        tree->sums[i]++;
        i += i & -i;
    }
}

// [1 ... to]
int fwt_sum_to(FenwickTree *tree, int to) {
    int s = 0;
    while (to > 0) {
        s += tree->sums[to];
        to -= to & (-to); 
    }
    return s;
}

void fwt_init(FenwickTree *tree, int size) {
    tree->sums = (int*)malloc((size+1)*sizeof(int));
    tree->sums[0] = 0;
    for (int i = 1; i <= size; i++) tree->sums[i] = i & (-i);
    tree->size = size;
}

void find_swaps_needed(int n, FenwickTree *fwt, int *index) {
    
    int top = n>>1;
    for (int i = 1; i <= top; i++) {
        
        int left = i;
        int li = index[left];
        printf("%d\n", fwt_sum_to(fwt, li) - i);
        fwt_increment(fwt, 1);
        fwt_decrement(fwt, li);

        int right = n+1-i;
        int ri = index[right];
        printf("%d\n", n - fwt_sum_to(fwt, ri) - i + 1);
        fwt_decrement(fwt, ri);
    }

    if (n&1) printf("0\n");
}

int main() {
    int n;
    scanf("%d", &n);

    FenwickTree fwt;
    fwt_init(&fwt, n);

    int tmp, index[n+1];
    for (int i = 1; i <= n; i++) {
        scanf("%d",&tmp);
        index[tmp] = i;
    }

    find_swaps_needed(n, &fwt, index);

    //free(fwt.sums);

    return 0;
}