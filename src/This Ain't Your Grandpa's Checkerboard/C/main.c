#include <stdio.h>
#include <string.h>

int is_valid(int n) {
    char rows[2][n+1];
    int v_cnt[n];
    int v_run[n];

    memset(v_cnt, 0, n*sizeof(int));
    memset(v_run, 0, n*sizeof(int));

    for (int i = 0; i < n; i++) {
        scanf("%s", rows[i & 1]);
        int h_cnt = 0;
        int h_run = 0;
        for (int j = 0; j < n; j++) {
            // Vertical runs
            if (i == 0 || rows[i&1][j] == rows[!(i&1)][j]) {
                v_run[j]++;
                if (v_run[j] == 3) return 0;
            } else {
                v_run[j] = 1;
            }

            // Horizontal runs
            if (j == 0 || rows[i&1][j] == rows[i&1][j-1]) {
                h_run++;
                if (h_run == 3) return 0;
            } else {
                h_run = 1;
            }

            // Counting
            if (rows[i&1][j] == 'W') {
                h_cnt++;
                v_cnt[j]++;
            }
        }
        if (h_cnt != (n >> 1)) return 0;
    }

    for (int i = 0; i < n; i++) {
        if (v_cnt[i] != (n>>1)) return 0;
    }

    return 1;
}

int main() {
    int n;
    scanf("%d",&n);
    printf("%d\n", is_valid(n));
    return 0;
}