#include "graph.h"

void graph_init(Graph *g, int v) {
    g->v = v;
    for (int i = 0; i < v; i++) {
        for (int j = 0; j < 2; j++) g->deg[i][j] = INIT_SET_EMPTY;
    }
}

void graph_add_edge(Graph *g, int v, int u) {
    set_add(&g->deg[v][OUT], u);
    set_add(&g->deg[u][IN], v);
}

void graph_remove_edge(Graph *g, int v, int u) {
    set_remove(&g->deg[v][OUT], u);
    set_remove(&g->deg[u][IN], v);
}

void graph_extend(Graph *g) {
    for (int i = 0; i < 2; i++) {
        g->deg[g->v][i] = INIT_SET_EMPTY;
    }
    g->v++;
}

void graph_disconnect_vertex(Graph *g, int v) {
    for (int i = 0; i < 2; i++) {
        g->deg[v][i] = INIT_SET_EMPTY;
    }
    for (int u = 0; u < g->v; u++) {
        for (int i = 0; i < 2; i++) {
            set_remove(&g->deg[u][i], v);
        }
    }
}

void in_out_swap(IntSet *a, IntSet *b) {
    IntSet tmp = *a;
    *a = *b;
    *b = tmp;
}

void graph_transpose(Graph *g) {
    for (int v = 0; v < g->v; v++) {
        in_out_swap(&g->deg[v][OUT],&g->deg[v][IN]);
    }
}

void graph_complement(Graph *g) {
    for (int v = 0; v < g->v; v++) {
        for (int i = 0; i < 2; i++) {
            set_complement_up_to(&g->deg[v][i], g->v);
            set_remove(&g->deg[v][i], v);
        }
    }
}

void graph_print(Graph *g) {
    ull pow7[MAX_V] = {1, [1 ... (MAX_V-1)] = 0};
    printf("%d\n", g->v);
    for (int v = 0; v < g->v; v++) {
        int out_deg = 0, index = 0;
        ull hash = 0;
        for (int u = 0; u < g->v; u++) {
            if (!pow7[index]) pow7[index] = (7*pow7[index-1]) % MOD;
            if (set_contains(&g->deg[v][OUT], u)) {
                hash = (hash + pow7[index++] * u) % MOD;
                out_deg++;
            }
        }
        printf("%d %llu\n", out_deg, hash);
    }
}

void graph_debug(Graph* g) {
    printf("-------------------------\n");
    printf("G = (V,E) where |V|=%d\n", g->v);
    for (int v = 0; v < g->v; v++) {
        printf("%d_out:", v);
        for (int u = 0; u < g->v; u++) {
            if (set_contains(&g->deg[v][OUT],u)) printf(" %d", u);
        }
        putchar('\n');
        printf("%d_in :", v);
        for (int u = 0; u < g->v; u++) {
            if (set_contains(&g->deg[v][OUT],u)) printf(" %d", u);
        }
        putchar('\n');
    }
    printf("-------------------------\n");
}