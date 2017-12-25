#include <stdio.h>
#include <stdint.h>

typedef struct
{
    uint32_t n, d;
} fraction;

void find_fraction(uint32_t node, fraction* frac)
{
    int bin = 0, start = 0;
    while(node != 1)
    {
        if (node & 1) bin |= (1 << start);
        start++;
        node >>= 1;
    }
    for (int i = start - 1; i >= 0; i--)
    {
        if (bin & (1 << i)) frac->n = frac->n + frac->d;
        else frac->d = frac->n + frac->d;
    }
}

int main()
{
    uint32_t n = 0;
    scanf("%u", &n);
    while(n--)
    {
        uint32_t c = 0, node = 0;
        scanf("%u %u", &c, &node);
        fraction frac = {1,1};
        find_fraction(node, &frac);
        printf("%u %u/%u\n", c, frac.n, frac.d);
    }
    return 0;
}