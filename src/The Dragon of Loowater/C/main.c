#include <stdio.h>
#include <stdlib.h>

int comparator(const void *a, const void *b) { return *(int*)a - *(int*)b; }

int cost(int n, int m, int *heads, int *knights) {
    if (m < n) return -1;
    qsort(heads, n, sizeof(int), comparator);
    qsort(knights, m, sizeof(int), comparator);
    
    int k = 0, c = 0;
    for (int h = 0; h < n; h++) {
        while(1) {
            if (k == m) return -1;
            if (knights[k] >= heads[h]) {
                c += knights[k++];
                break;
            }
            k++;
        }
    }
    return c;
}

int main() {
    while(1) {
        int n,m,c;
        scanf("%d %d", &n, &m);
        if (n==0 && m==0) break;
        int heads[n], knights[m];
        for (int i = 0; i < n; i++) scanf("%d", heads + i);
        for (int i = 0; i < m; i++) scanf("%d", knights + i);
        if ((c = cost(n,m,heads,knights))==-1) printf("Loowater is doomed!\n");
        else printf("%d\n", c);
    }

    return 0;
}