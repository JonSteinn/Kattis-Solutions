#include <stdio.h>

/*
 * let n be the equal point, then
 * yn + x = n => n(y-1) = -x => n = x / (1 - y)
 */

int main()
{
    int x, y;
    scanf("%d %d", &x, &y);
    if (x == 0 && y == 1) printf("ALL GOOD\n");
    else if (y == 1) printf("IMPOSSIBLE\n");
    else printf("%.6f\n", x / (1.0 - y));
    return 0;
}