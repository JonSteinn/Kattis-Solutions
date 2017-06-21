#include <stdio.h>

int lpd(int n)
{
    if (n == 1) return 1;
    if (!(n & 1)) return n >> 1;
    if (n % 3 == 0) return n / 3;
    int largest = n >> 1;
    int r = largest % 6;
    if (r != 5)
    {
        while(1)
        {
            if (r == -1) break;
            if (n % largest == 0) return largest;
            largest--;
            r--;
        }
    }
    for (int i = largest; i >= 5; i -= 6)
    {
        if (n % (i + 2) == 0) return i + 2;
        if (n % i == 0) return i;
    }
    return 1;
}

int main()
{
    int n;
    scanf("%d",&n);
    printf("%d\n", n - lpd(n));
    return 0;
}