#include <stdio.h>

int main()
{
    int n;
    while (scanf("%d", &n) == 1) printf("%d\n", n < 2 ? n : 2 * (n - 1));
    return 0;
}