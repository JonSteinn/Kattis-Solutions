#include <stdio.h>

int main()
{
    unsigned long long n;
    int b;
    scanf("%llu %d", &n, &b);
    printf(n > (1LLU << (b+1)) - 1 ? "no\n" : "yes\n");
    return 0;
}