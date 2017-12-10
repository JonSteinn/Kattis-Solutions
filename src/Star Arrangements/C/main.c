#include <stdio.h>

int main()
{
    int s;
    scanf("%d", &s);
    int top = (s>>1) + ((s&1) ? 2 : 1);
    printf("%d:\n", s);
    for (int i = 2; i < top; i++)
    {
        int rem = s % ((i << 1) - 1);
        if (rem == 0 || rem == i) printf("%d,%d\n", i, i - 1);
        if (s % i == 0) printf("%d,%d\n", i, i);
    }
    return 0;
}