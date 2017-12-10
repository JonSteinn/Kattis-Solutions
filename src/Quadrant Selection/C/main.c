#include <stdio.h>

int main() {
    int x,y;
    scanf("%d %d", &x, &y);
    printf("%d", x < 0 ? (y < 0 ? 3 : 2) : (y < 0 ? 4 : 1));
    return 0;
}