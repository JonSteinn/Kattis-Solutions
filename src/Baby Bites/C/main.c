#include <stdio.h>
#include <stdlib.h>

int valid(int n) {
    for (int i = 0; i < n; i++) {
        char next[7];
        scanf("%s", next);
        if (next[0] != 'm' && atoi(next) != i + 1) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);
    printf(valid(n) ? "makes sense\n" : "something is fishy\n");
    return 0;
}