#include <stdio.h>

int main()
{
    int x, y;
    scanf("%d %d", &x, &y);
    printf(y&1 ? "impossible\n" : "possible");
    return 0;
}