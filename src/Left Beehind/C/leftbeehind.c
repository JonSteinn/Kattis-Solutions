#include <stdio.h>

int main()
{
    while (1)
    {
        int x, y;
        scanf("%d %d", &x, &y);
        if (x == 0 && y == 0) break;
        if (x + y == 13) printf("Never speak again.\n");
        else if (x > y) printf("To the convention.\n");
        else if (x < y) printf("Left beehind.\n");
        else printf("Undecided.\n");
    }
    return 0;
}