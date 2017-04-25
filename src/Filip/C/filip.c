#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    a = (a % 10) * 100 + ((a / 10) % 10) * 10 + ((a / 100) % 10);
    b = (b % 10) * 100 + ((b / 10) % 10) * 10 + ((b / 100) % 10);
    printf("%d\n", a < b ? b : a);
    return 0;
}