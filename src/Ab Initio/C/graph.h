#include <stdio.h>
#include "set.h"

#define MOD 1000000007
#define MAX_V 4000
#define OUT 0
#define IN 1

typedef unsigned long long ull;

typedef struct {
    int v;
    IntSet deg[MAX_V][2];
} Graph;

void graph_init(Graph *g, int v);
void graph_add_edge(Graph *g, int v, int u);
void graph_remove_edge(Graph *g, int v, int u);
void graph_extend(Graph *g);
void graph_disconnect_vertex(Graph *g, int v);
void in_out_swap(IntSet *a, IntSet *b);
void graph_transpose(Graph *g);
void graph_complement(Graph *g);
void graph_print(Graph *g);
void graph_debug(Graph* g);