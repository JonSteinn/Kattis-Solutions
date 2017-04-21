#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

/*
 * We are looking for the number y = n! given n!.
 *
 * The number of digits in a number x is
 *      log(x)+1 if x is a power of 10
 *      ceil(log(x)) otherwise
 * The only factorial numbers that are a power of 10 are 0! and 1!
 * since 2! isn't and the rest have 3 as a factor.
 *
 * After 9!, each number is the previous multiplied by at least 10
 * which makes it's digit count unique. There are some non-unique
 * digit counts in the early numbers:
 * 0! = 1
 * 1! = 1
 * 2! = 2
 * 3! = 6
 * 4! = 24
 * 5! = 120
 * 6! = 720
 * 7! = 5040
 * 8! = 40320
 * 9! = 936880
 *
 * Now we only need to check when we have reached the same number of
 * digits as our desired number and to do that, we can use the
 * following identity:
 *      log(n!) = log(1 * 2 * ... * n) = log(1) + log(2) + ... + log(n)
 */

int pre_defined(int n)
{
    return n == 1 ? 1 : n == 2 ? 2 : n == 6 ? 3 : n == 24 ? 4 : n == 120 ? 5 : 6;
}

int main()
{
    char buffer[1000001];
    scanf("%s", buffer);
    size_t digits = strlen(buffer);

    if (digits < 4)
    {
        printf("%d\n", pre_defined(atoi(buffer)));
    }
    else
    {
        int number = 6;
        double log_sum = 4 * log10(2) + 2 * log10(3) + log10(5);
        while (1)
        {
            log_sum += log10(++number);
            if (log_sum > digits)
            {
                printf("%d\n", number - 1);
                break;
            }
        }
    }
    return 0;
}