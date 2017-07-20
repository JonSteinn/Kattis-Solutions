#include <stdio.h>

int main()
{
    int s, v1, v2;
    scanf("%d %d %d", &s, &v1, &v2);
    if (v1 < v2) v1 ^= v2 ^= v1 ^= v2;
    int found = 0;
    for (int i = s / v1; i >= 0; i--)
    {
        int rem = s - i * v1;
        if (rem % v2 == 0)
        {
            printf("%d %d\n", i, rem / v2);
            found = 1;
            break;
        }
    }
    if (!found) printf("Impossible\n");
    return 0;
}