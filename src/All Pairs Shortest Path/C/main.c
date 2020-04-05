#include <stdio.h>
#include <string.h>

// Large enough, and allows me to use memset
#define INF 0b01111111011111110111111101111111

int main() {
    int first_test_case = 1;
    while(1) {
        int n,m,q;
        scanf("%d %d %d", &n, &m, &q);
        if (n+m+q== 0) break;

        if (first_test_case) {
            first_test_case = 0;
        } else {
            putchar('\n');
        }

        int mat[n][n];
        int neg_cycle[n][n];
        int neg_mem[n][n];
        memset(mat, 0b01111111, sizeof(mat));
        memset(neg_cycle, 0, sizeof(neg_cycle));
        memset(neg_mem, 0, sizeof(neg_mem));

        for (int i = 0; i < n; i++) mat[i][i] = 0;
        for (int i = 0; i < m; i++) {
            int u,v,w;
            scanf("%d %d %d", &u, &v, &w);
            if ((u != v || w < 0) && mat[u][v] > w) mat[u][v]=w;
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (mat[i][k] != INF && mat[k][j] != INF && mat[i][j] > mat[i][k] + mat[k][j]) {
                        mat[i][j] = mat[i][k] + mat[k][j];
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            neg_mem[i][i] = 1;
            neg_cycle[i][i] = mat[i][i] < 0;
        }

        for (int i = 0; i < q; i++) {
            int u, v;
            scanf("%d %d", &u, &v);

            if (mat[u][v] == INF) {
                printf("Impossible\n");
            } else if (neg_mem[u][v]) {
                if (neg_cycle[u][v]) printf("-Infinity\n");
                else printf("%d\n", mat[u][v]);
            } else {
                int neg = 0;
                for (int s = 0; s < n; s++) {
                    if (s==u || s==v) continue;
                    if (mat[u][s] != INF && mat[s][v] != INF && neg_cycle[s][s]) {
                        neg = 1;
                        neg_cycle[u][v] = 1;
                        break;
                    }
                }
                if (!neg) neg_cycle[u][v] = 0;
                neg_mem[u][v] = 1;

                if (neg) printf("-Infinity\n");
                else printf("%d\n", mat[u][v]);
            }
        }
    }

    return 0;
}