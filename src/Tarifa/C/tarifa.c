#include <stdio.h>

int main()
{
    int monthly;
    scanf("%d", &monthly);

    int n;
    scanf("%d", &n);

    int total = 0, i;
    for (i = 0; i < n; i++)
    {
        int next;
        scanf("%d", &next);
        total += next;
    }

    printf("%d\n", (n + 1) * monthly - total);

    return 0;
}