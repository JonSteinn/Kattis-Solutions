#include <stdio.h>

int main()
{
    int b,k,g, groups;
    scanf("%d %d %d",&b,&k,&g);
    printf("%d\n", (b - 1) % (groups = k / g) == 0 ? (b - 1) / groups : (b - 1) / groups + 1);
    return 0;
}