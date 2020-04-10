#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/time.h>
#include <time.h> 

#define TIME_LIMIT 1.99
#define BOUNDARY 20
#define INF 2147483647

typedef struct {
    double x,y;
} Point;

typedef struct {
    int* dist;
    int* mem;
    int n;
} hk_param;

void construct_path_from_held_karp(int* path, int n, int* mem, int* dist, int best) {
    int s = 1;
    path[0] = 0;
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            if (s & (1 << j)) continue;
            int offset = j*(1<<n), next_set = s | (1<<j);
            if (best == (mem + offset)[next_set] + (dist+j*n)[path[i-1]]) {
                best = (mem + offset)[next_set];
                path[i] = j;
                s = next_set;
                break;
            }
        }
    }
}

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

void exact(int n, int* path, int* dist) {
    int mem[n*(1<<n)];
    memset(mem,-1,sizeof(mem));
    hk_param args = {dist,mem,n};
    int best = held_karp(&args, 0, 1);
    construct_path_from_held_karp(path,n,mem,dist,best);
}

// Use the time for something (even though the gain is small) 
// until better approx is implemented...
// Stochastic... so hard to say... but managed score of 7 (up from 5.9)
void random_updates(int n, int* tour, int best, int* dist) {
    srand(time(0));
    struct timeval start, stop;
    gettimeofday(&start, NULL);
    double secs = 0;
    while (1) {

        gettimeofday(&stop, NULL);
        secs = (double)(stop.tv_usec - start.tv_usec) / 1000000 + (double)(stop.tv_sec - start.tv_sec);
        if (secs > TIME_LIMIT) break;

        int from = 1+(rand() % (n-1)), to = 1+(rand() % (n-1)); // {1,2,...,n-1}
        while (from == to) {
            from = 1+(rand() % (n-1));
            to = 1+(rand() % (n-1));
        }

        int new_len = 0;
        tour[from] ^= tour[to] ^= tour[from] ^= tour[to];
        for (int i = 1; i < n; i++) new_len += (dist+tour[i-1]*n)[tour[i]];
        new_len += (dist + tour[n-1]*n)[0];

        if (new_len < best) {
            best = new_len;
        } else {
            tour[from] ^= tour[to] ^= tour[from] ^= tour[to];
        }
    }
}

// TODO: Simulated annealing (or check if MCTS can be useful)
void approx(int n, int* tour, int* dist) {
    int total = 0;

    // Greedily select the closest city next, starting with city 0.
    int* used = (int*)calloc(n, sizeof(int));
    tour[0] = 0;
    used[0] = 1;
    for (int i = 1; i < n; i++) {
        int best = -1;
        int best_val = -1;
        for (int j = 0; j < n; j++) {
            if (!used[j] && (best == -1 || (dist+n*tour[i-1])[j] < (dist+n*tour[i-1])[best])) {
                best = j;
                best_val = (dist+n*tour[i-1])[j];
            }
        }
        tour[i] = best;
        total += best_val;
        used[best] = 1;
    }
    free(used);
    total += (dist+n*tour[n-1])[0];
    random_updates(n,tour,total,dist);
}

void fill_dist(int n, int* arr) {
    Point pts[n];
    for (int i = 0; i < n; i++) scanf("%lf %lf", &pts[i].x, &pts[i].y);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                (arr + i*n)[j] = 0;
            } else {
                double dx = pts[i].x - pts[j].x;
                double dy = pts[i].y - pts[j].y;
                int val = (int)(0.5+sqrt(dx*dx + dy*dy));
                (arr + i*n)[j] = val;
                (arr + j*n)[i] = val;
            }
        }
    }
}

int main() {
    int n;
    scanf("%d",&n);
    int dist[n*n];
    fill_dist(n, dist);
    int path[n];
    if (n > BOUNDARY) approx(n, path, dist);
    else exact(n, path, dist);
    for (int i = 0; i < n; i++) printf("%d\n", path[i]);
    return 0;
}