#include <stdio.h>

int main() 
{
    int n, k, r, s = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < k; i++)
    {
        scanf("%d", &r);
        s += r;
    }
    printf("%.4f %.4f\n", (s - 3.0 * (n - k)) / n, (s + 3.0 * (n - k)) / n); 
    return 0;
}