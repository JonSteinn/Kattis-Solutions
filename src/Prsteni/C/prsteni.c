#include <stdio.h>

int gcd(int a, int b)
{
    while(b) b ^= a ^= b ^= a %= b;
    return a;
}

int main()
{
    int n;
    scanf("%d", &n);
    n--;
    int first;
    scanf("%d", &first);
    while (n-- > 0)
    {
        int next;
        scanf("%d", &next);
        int g = gcd(first, next);
        printf("%d/%d\n", first / g, next / g);
    }
    return 0;
}