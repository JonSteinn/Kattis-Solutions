#include <stdio.h>

int main()
{
    int n = 0;
    scanf("%d", &n);
    printf("%d\n", n >> 2 ? n - 2 : 1);
    return 0;
}