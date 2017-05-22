#include <stdio.h>

int main()
{
    int b, b_r, b_s, a, a_s;
    scanf("%d %d %d %d %d", &b, &b_r, &b_s, &a, &a_s);
    printf("%d\n", (int)((b_r - b) * b_s / (double)a_s + a) + 1);
    return 0;
}