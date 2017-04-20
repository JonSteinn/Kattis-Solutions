#include <stdio.h>
int main()
{
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    int diff1 = b-a, diff2 = c-b;
    printf("%d", (diff1 < diff2) ? (diff2-1) : (diff1-1));
    return 0;
}