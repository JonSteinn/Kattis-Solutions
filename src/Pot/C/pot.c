#include <stdio.h>

int ipow(int base, int exp)
{
    int result = 1;
    while (exp)
    {
        if (exp & 1) result *= base;
        exp >>= 1;
        base *= base;
    }
    return result;
}

int main()
{
    int n, next, sum = 0;
    scanf("%d", &n);
    while (n-- > 0)
    {
        scanf("%d", &next);
        sum += ipow(next / 10, next % 10);
    }
    printf("%d\n", sum);
    return 0;
}