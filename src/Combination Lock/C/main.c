#include <stdio.h>

int main()
{
    int s, a, b, c;
    while(1)
    {
        scanf("%d %d %d %d", &s, &a, &b, &c);
        if (!s && !a && !b && !c) break;
        printf("%d\n", (120 + (s - a + 40) % 40 + (b - a + 40) % 40 + (b - c + 40) % 40) * 9);
    }
    return 0;
}