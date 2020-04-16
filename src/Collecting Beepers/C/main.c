#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 2147483647

typedef struct {
    int x,y;
} Point;

typedef struct {
    int* dist;
    int* mem;
    int n;
} hk_param;

int held_karp(hk_param* args, int i, int s) {
    int m_offset = i*(1<<args->n);
    if ((args->mem+m_offset)[s] == -1) {
        int best = INF, d_offset = i*args->n;
        if (s == ((1 << args->n) - 1)) {
            best = (args->dist + d_offset)[0];
        } else {
            for (int j = 0; j < args->n; j++) {
                if (s & (1 << j)) continue;
                int dive = (args->dist+d_offset)[j] + held_karp(args, j, s | (1 << j));
                if (dive < best) best = dive;
            }
        }
        (args->mem+m_offset)[s] = best;
    }
    return (args->mem+m_offset)[s];
}

int tsp(int n, int* dist) {
    int mem[n*(1<<n)];
    memset(mem,-1,sizeof(mem));
    hk_param args = {dist,mem,n};
    return held_karp(&args, 0, 1);
}

void fill_dist(int n, int* arr, int x, int y) {
    Point pts[n];
    pts[0] = (Point){x,y};
    for (int i = 1; i < n; i++) scanf("%d %d", &pts[i].x, &pts[i].y);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                (arr + i*n)[j] = 0;
            } else {
                int val = abs(pts[i].x - pts[j].x) + abs(pts[i].y - pts[j].y);
                (arr + i*n)[j] = val;
                (arr + j*n)[i] = val;
            }
        }
    }
}

int main() {
    int tc;
    scanf("%d", &tc);
    while(tc--) {
        int x,y;
        scanf("%d %d", &x, &y); // dump dim since we don't care
        scanf("%d %d", &x, &y);
        int n;
        scanf("%d", &n);
        n++;
        int dist[n*n];
        fill_dist(n, dist, x, y);
        printf("%d\n", tsp(n, dist));
    }
    return 0;
}