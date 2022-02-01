#include <stdio.h>

int main() 
{
    int n;
    scanf("%d", &n);
    while (n--)
    {
        int k;
        scanf("%d", &k);

        int sum = -k + 1;
        for (int i = 0; i < k; i++)
        {
            int nxt;
            scanf("%d", &nxt);
            sum += nxt;
        }
        printf("%d\n", sum);
    }
    return 0;
}