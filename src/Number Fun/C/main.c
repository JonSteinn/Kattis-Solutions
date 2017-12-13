#include <stdio.h>

int can_produce(int a, int b, int c)
{
    if (a + b == c) return 1;
    if (a - b == c) return 1;
    if (b - a == c) return 1;
    if (a * b == c) return 1;
    int d = a / b;
    if (d == c && d * b == a) return 1;
    d = b / a;
    if (d == c && d * a == b) return 1;
    return 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    while(n--)
    {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        printf(can_produce(a, b, c) ? "Possible\n" : "Impossible\n");
    }
    return 0;
}