#include <stdio.h>

// (r1+r2)/2 = s => 2s = r1+r2 => r2 = 2s-r1

int main()
{
    int r, s;
    scanf("%d %d", &r, &s);
    printf("%d\n", (s<<1)-r);
    return 0;
}