#include <stdio.h>
#include <string.h>
#include <stdint.h>

#define SIZE 300001
#define MAX_JUMP_SIZE 19

int front[SIZE];
int ancestors[SIZE][MAX_JUMP_SIZE];
int depth[SIZE];
int eq[SIZE];

void init_arrays(int n) {
    memset(eq, -1, sizeof(int) * (n+1));
    depth[0] = 0;
}

int get_eq(int v) {
    while (eq[v] != -1) {
        if (eq[eq[v]] != -1) eq[v] = eq[eq[v]];
        v = eq[v];
    }
    return v;
}

int get_kth_ancestor_of(int k, int v) {
    int steps = 32-__builtin_clz(k)-1;
    return (k == 1<<steps) ? ancestors[v][steps] : get_kth_ancestor_of(k & ~(1<<steps), ancestors[v][steps]);
}

int find_common_from_same_depth(int v, int w) {
    if (w == v) return w;
    if (ancestors[w][0] == ancestors[v][0]) return ancestors[w][0];
    for (int steps = 32-__builtin_clz(depth[w])-1; steps > 0; steps--) {
        int a_v = ancestors[v][steps], a_w = ancestors[w][steps];
        if (a_v != a_w) return find_common_from_same_depth(a_v, a_w);
    }
    return find_common_from_same_depth(ancestors[v][0], ancestors[w][0]);
}

int least_common_ancestor(int v, int w) {
    if (depth[v] - depth[w]) {
        if (depth[v] < depth[w]) v ^= w ^= v ^= w;
        v = get_kth_ancestor_of(depth[v]-depth[w], v);
    }
    return find_common_from_same_depth(v, w);
}

void a(int i, int v) {
    ancestors[i][0] = v;
    front[i] = i;
    depth[i] = depth[v] + 1;
    int top = 32-__builtin_clz(depth[i]); 
    for (int j = 1; j < top; j++) ancestors[i][j] = ancestors[ancestors[i][j-1]][j-1];
}

int b(int i, int v) {
    eq[i] = get_eq(ancestors[v][0]);
    return front[v];
}

int c(int i, int v, int w) {
    return depth[least_common_ancestor(eq[i] = v,w)];
}

int main() {
    int n,v,w;
    char op;
    scanf("%d",&n);
    init_arrays(n);
    for (int i = 1; i <= n; i++) {
        scanf(" %c %d", &op, &v);
        switch(op) {
            case 'a':
                a(i,get_eq(v));
                break;
            case 'b':
                printf("%d\n", b(i,get_eq(v)));
                break;
            default:
                scanf("%d", &w);
                printf("%d\n", c(i,get_eq(v),get_eq(w)));
        }
    }
    return 0;
}