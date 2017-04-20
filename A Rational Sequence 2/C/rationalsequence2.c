#include <stdio.h>

struct fraction
{
    int n, d;
};

void experiment()
{
    int e;
    scanf("%d", &e);
    struct fraction frac;
    scanf("%d/%d", &frac.n, &frac.d);

    int path = 0; // array of bits
    int path_index = 0;

    // Backtrack
    while (frac.d != frac.n)
    {
        if (frac.d > frac.n)
        {
            frac.d -= frac.n;
        }
        else
        {
            frac.n -= frac.d;
            path |= (1 << path_index);
        }
        path_index++;
    }

    int i, result = 1;
    for (i = path_index - 1; i >= 0; i--)
    {
        if (path & (1 << i)) result = (result << 1) + 1;
        else result <<= 1;
    }
    printf("%d %d\n", e, result);
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n-- > 0) experiment();
    return 0;
}