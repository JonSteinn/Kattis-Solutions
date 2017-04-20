#include <stdio.h>

int main()
{
    int n, T;
    scanf("%d %d", &n, &T);
    int next, sum = 0, total = 0;
    while (n-- > 0)
    {
        scanf("%d", &next);
        if ((total += next) <= T) sum++;
        else break;
    }
    while (n-- > 0) scanf("%d", &next);
    printf("%d\n", sum);
    return 0;
}