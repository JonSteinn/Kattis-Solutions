#include "string.h"
#include "stdio.h"

int root(int level)
{
    return (1 << (level + 1)) - 1;
}

void travel_down(int* number, char dir, int root_plus_one)
{
    *number = root_plus_one - (((root_plus_one - *number) << 1) + (dir == 'R' ? 1 : 0));
}

int main()
{
    int n;
    scanf("%d", &n);
    char buffer[n + 1];
    n = root(n);
    if (scanf("%s", buffer) == EOF) printf("%d\n", n);
    else
    {
        int root_plus_one = n + 1;
        int i, len = strlen(buffer);
        for (i = 0; i < len; i++) travel_down(&n, buffer[i], root_plus_one);
        printf("%d\n", n);
    }

    return 0;
}