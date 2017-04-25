#include <stdio.h>
#include <math.h>

void perfect(int n)
{
    int sq = (int)sqrt(n) + 1;
    int sum = 1;
    for (int i = 2; i < sq; i++)
    {
        if (n % i == 0)
        {
            int other = n / i;
            if (i != other) sum += other;
            sum += i;
        }
    }
    printf(sum == n ? "%d perfect\n" : (abs(sum - n) < 3) ? "%d almost perfect\n" : "%d not perfect\n", n);

}

int main()
{
    int n;
    while (scanf("%d", &n) == 1) perfect(n);
    return 0;
}