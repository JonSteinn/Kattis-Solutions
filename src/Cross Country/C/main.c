#include <stdio.h>

int main() {
    int n,s,t;
    scanf("%d %d %d", &n, &s, &t);

    int d[n][n];
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            scanf("%d", &d[r][c]);
        }
    }
    
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int shortcut = d[i][k] + d[k][j];
                if (shortcut < d[i][j]) d[i][j] = shortcut;
            }
        }
    }
    
    printf("%d\n", d[s][t]);

    return 0;
}