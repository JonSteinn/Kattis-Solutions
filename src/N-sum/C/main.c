#include <stdio.h>

int main() 
{
    int n, nxt, s = 0;
    scanf("%d", &n);
    while(n--)
    {
        scanf("%d", &nxt);
        s += nxt;
    }
    printf("%d\n", s);
    return 0;
}