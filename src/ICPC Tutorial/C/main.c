#include <stdio.h>
#include <math.h>

#define MAX_FACTORIAL 12
#define EPSILON 1E-6
int factorials[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600};

int accepted(int m, int n, int t)
{
    return t == 1 ? (n > MAX_FACTORIAL || factorials[n] > m) ? 0 : 1 :
           t == 2 ? n <= log2(m) + EPSILON :
           t == 3 ? n <= pow(m, 0.25) + EPSILON :
           t == 4 ? n <= pow(m, 0.333333333333333333333333333333333333333333333333333333) + EPSILON :
           t == 5 ? n <= pow(m, 0.5) + EPSILON :
           t == 6 ? n * log2(n) <= m + EPSILON :
                    n <= m;
}

int main()
{
    int m,n,t;
    scanf("%d %d %d",&m,&n,&t);
    printf(accepted(m,n,t) ? "AC\n" : "TLE\n");
    return 0;
}