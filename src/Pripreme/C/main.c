#include <stdio.h>
#include <stdint.h>

int main()
{
    int32_t n;
    scanf("%d",&n);

    if (n == 1)
    {
        scanf("%d",&n);
        printf("%d\n",n);
    }
    else
    {
        // If there are more than 1 we can...
        // Pick the two largest groups (in terms of time needed) and rotate
        // between them until one changes. Repeat until none left.
        // The exception to this is when one is larger then the rest.

        // example
        // 5 6 3
        // 4 5 3
        // 3 4 3
        // 2 3 3
        // 2 2 2
        // 1 1 2
        // 0 1 1
        // 0 0 0

        // If all times are 3 * 10^5 as well as n, we have (3 * 10^5)^2 > int_max so we need ull
        uint64_t total = 0;
        int32_t max = -1;
        while(n--)
        {
            int next;
            scanf("%d",&next);
            if (next > max) max = next;
            total += next;
        }
        uint64_t rest = total - max;
        printf("%llu\n", rest < max ? max<<1 : total);
    }
    return 0;
}