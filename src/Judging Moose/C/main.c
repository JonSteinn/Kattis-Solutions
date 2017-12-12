#include <stdio.h>

int main()
{
    int l, r;
    scanf("%d %d", &l, &r);
    if (!l && !r) printf("Not a moose\n");
    else if (l-r) printf("Odd %d\n", l < r ? r << 1 : l << 1);
    else printf("Even %d\n", l << 1);
    return 0;
}