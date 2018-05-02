#include <stdio.h>

int main()
{
    while(1)
    {
        int a = 0, b = 0, c = 0;
        scanf("%d %d %d", &a, &b, &c);
        if (!a) break;
        if (a > b) a^=b^=a^=b;
        if (b > c) b^=c^=b^=c;
        if (a > b) a^=b^=a^=b;
        printf(a * a + b * b - c * c ? "wrong\n" : "right\n");
    }
    return 0;
}