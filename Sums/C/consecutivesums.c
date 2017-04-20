#include <stdio.h>

/* (a) + (a+1) + (a+2) + ... + (b-1) + (b) */
int sum_ab(int a, int b)
{
    return (b * (b + 1) - a * (a - 1)) >> 1;
}

/* Check if a+...+b or (a+1)+...(b+1) is equal to n */
int check_sum(int n, int k, int start)
{
    return sum_ab(start + 1, start + k) == n ? start + 1 : sum_ab(start, start + k - 1) == n ? start : 0;
}

/* Start from k=2 and check if sum containing n/k in middle 
 * (check sum handles the odd/even cases) is equal to n. We
 * are guaranteed to find a solution here so loop goes until
 * one is one is found.
 */
void sum_search(int n)
{
    int k = 2, result;
    while (!(result = check_sum(n, k, n / k - (k >> 1)))) k++;
    printf("%d = %d", n, result);
    for (n = 1; n < k; n++) printf(" + %d", result + n);
    printf("\n");
}

int main()
{
    int times, number;
    scanf("%d", &times);
    while (times-- > 0)
    {
        scanf("%d", &number);
        if (number & (number - 1)) sum_search(number);
        else printf("IMPOSSIBLE\n"); // impossible for {2^i | i in N}
    }
}