#include <stdio.h>

/*
 * Given n characters, there are 2^n subsets, n of which are singletons and 1 empty.
 * Therefore we need 2^n - n - 1 relations to develop or (1<<n)-n-1.
 */

int main()
{
    int n;
    scanf("%d",&n);
    printf("%d", (1 << n) - n - 1);
    return 0;
}