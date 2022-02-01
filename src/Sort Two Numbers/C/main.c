#include <stdio.h>

int main() 
{
    int a, b;
    scanf("%d %d", &a, &b);
    if (b < a) a ^= b ^= a ^= b;
    printf("%d %d\n", a, b);
    return 0;
}