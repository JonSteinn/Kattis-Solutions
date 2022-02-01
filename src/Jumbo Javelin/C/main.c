#include <stdio.h>

int main() 
{
    int n, k, s = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &k);
        s += k;
    }
    printf("%d\n", s - n + 1);
    return 0;
}