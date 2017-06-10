#include <stdio.h>

int main()
{
    int x, y, i = 1;
    while (scanf("%d %d", &x, &y) == 2) printf("Case %d: %d\n", i++, (x = 11679*x-11680*y)<0 ? (x+(x/-250755+1)*250755)%250755 : x%250755);
    return 0;
}
