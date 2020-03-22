#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int root(int* p, int a) {
    while (p[a] >= 0) a = p[a];
    return a;
}

void connect(int* p, int a, int b) {
    int rA = root(p,a), rB = root(p, b);
    if (rA == rB) return;
    if (p[rA] > p[rB]) rA ^= rB ^= rA ^= rB;
    p[rA] += p[rB];
    p[rB] = rA;
}

int size_of(int* p, int a) {
    return -p[root(p,a)];
}

int main() {
    int n,q,a,b;
    char c;
    scanf("%d %d", &n, &q);
    int arr[n];
    memset(arr, 0xFF, n*sizeof(int));
    while(q--) {
        scanf(" %c %d", &c, &a);
        if (c=='t') {
            scanf("%d", &b);
            connect(arr, a-1, b-1);
        } else {
            printf("%d\n", size_of(arr, a-1));
        }
    }
    return 0;
}