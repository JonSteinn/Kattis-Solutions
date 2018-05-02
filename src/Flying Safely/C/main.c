#include <stdio.h>

int main()
{
    int tc = 0;
    scanf("%d", &tc);
    while(tc--)
    {
        int a = 0, b = 0, c = 0;
        scanf("%d %d", &a, &b);
        printf("%d\n", a - 1);
        while(b--) scanf("%d %d", &a, &c); // dump
    }
    return 0;
}