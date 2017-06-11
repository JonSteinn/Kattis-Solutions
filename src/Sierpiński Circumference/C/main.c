#include <stdio.h>
#include <math.h>

// f(n) = 3^(n+1) / 2^n
//      = 3 * 3^n / 2^n
//      = 3 * (3/2)^n
// log(f(n)) = log(3 * (3/2)^n)
//           = log(3) + log((3/2)^n)
//           = log(3) + n * log(3/2)

#define LOG3 0.4771212547196624372950279032551153092001288641907
#define LOG3_2 0.17609125905568124208128900853062228243193898272859

int main()
{
    int n, tc = 1;
    while(scanf("%d",&n) == 1) printf("Case %d: %d\n", tc++, (int)(LOG3 + n * LOG3_2) + 1);
    return 0;
}