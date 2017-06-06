#include <stdio.h>

int start_div(int n)
{
    if (n > 999999999)  return 1000000000;
    if (n > 99999999)   return 100000000;
    if (n > 9999999)    return 10000000;
    if (n > 999999)     return 1000000;
    if (n > 99999)      return 100000;
    if (n > 9999)       return 10000;
    if (n > 999)        return 1000;
    if (n > 99)         return 100;
    if (n > 9)          return 10;
    return 1;
}

int count_ones(int n)
{
    int counter = 0;
    while (n)
    {
        counter += n & 1;
        n >>= 1;
    }
    return counter;
}

int max_ones(int n)
{
    int div = start_div(n);
    int most = count_ones(n / div);
    div /= 10;
    while (div)
    {
        int next = count_ones(n / div);
        if (next > most) most = next;
        div /= 10;
    }
    return most;
}

int main()
{
    int n;
    scanf("%d",&n);
    while (n--)
    {
        int numb;
        scanf("%d",&numb);
        printf("%d\n", max_ones(numb));
    }
    return 0;
}