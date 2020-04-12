#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int r, c;
} Pos;


int r_comparator(const void* lhs, const void* rhs) {
    return ((Pos*)lhs)->r - ((Pos*)rhs)->r;
}

int c_comparator(const void* lhs, const void* rhs) {
    return ((Pos*)lhs)->c - ((Pos*)rhs)->c;
}

int move_rows(Pos* pos, int n) {
    qsort(pos, n, sizeof(Pos), r_comparator);
    int moves = 0;
    for (int i = 0; i < n; i++) moves += abs(i+1-pos[i].r);
    return moves;
}

int move_columns(Pos* pos, int n) {
    qsort(pos, n, sizeof(Pos), c_comparator);
    int moves = 0;
    for (int i = 0; i < n; i++) moves += abs(i+1-pos[i].c);
    return moves;
}

int main() {
    int n;
    scanf("%d",&n);

    Pos pos[n];
    for (int i = 0; i < n; i++) scanf("%d %d", &pos[i].r, &pos[i].c);

    int moves = move_rows(pos, n) + move_columns(pos, n);
    printf("%d\n", moves);

    return 0;
}