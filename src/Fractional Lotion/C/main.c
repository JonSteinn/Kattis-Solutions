#include <stdio.h>
#include <stdlib.h>

/*
 * Both are positive so sum must consist of two numbers lower than the original (higher denominator)
 * 1/(2n+1) + 1/(2n+1) = 2/(2n+1) = 1 / (n + 0.5) < 1/n and from there on, we will just decrease
 *
 *    1/x + 1/y = 1/n
 * => 1/x - 1/n = -1/y
 * => 1/y = 1/n - 1/x
 * => y = 1/(1/n - 1/x) = 1 / ((x-n) / (nx)) = nx/(x-n)
 */

int main()
{
    char buffer[8];
    while (scanf("%s",buffer) == 1)
    {
        int n = atoi(buffer+2);
        int counter = 0;
        int bound = (n << 1) + 1;
        for (int x = n+1; x < bound; x++)
        {
            int y = x * n; // / (x-n)
            if (y % (x - n) == 0) counter++;
        }
        printf("%d\n",counter);
    }
    return 0;
}