#include <stdio.h>
#include "graph.h"

void queries(Graph *g, int q) {
    int action, v, u;
    while (q--) {
        scanf("%d", &action);
        switch (action) {
            case 1:
                graph_extend(g);
                break;
            case 2:
                scanf("%d %d", &v, &u);
                graph_add_edge(g, v, u);
                break;
            case 3:
                scanf("%d", &v);
                graph_disconnect_vertex(g, v);
                break;
            case 4:
                scanf("%d %d", &v, &u);
                graph_remove_edge(g,v,u);
                break;
            case 5:
                graph_transpose(g);
                break;
            default: // 6
                graph_complement(g);
                break;
        }
        //graph_debug(g);
    }
}

int main() {
    int v, e, q, a, b;
    scanf("%d %d %d", &v, &e, &q);

    Graph g;
    graph_init(&g, v);

    while(e--) {
        scanf("%d %d", &a, &b);
        graph_add_edge(&g, a, b);
    }

    queries(&g, q);

    graph_print(&g);

    return 0;
}
