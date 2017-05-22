#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int k;
        scanf("%d",&k);

        double max = -INFINITY;
        int max_i = 0;

        for (int i = 1; i <= k; i++)
        {

            int a, b, c;
            scanf("%d %d %d", &a, &b, &c);

            // f(x) = -ax^2+bx+c => f'(x) = -2ax+b => [ f'(x) = 0 <=> x = b/(2a) ] 
            // and -a < 0 for all a > 1 so max in b/(2a)
            double der = (double)b/(a<<1);
            double val = -a * der * der + b * der + c;

            if (val > max)
            {
                max = val;
                max_i = i;
            }
        }

        printf("%d\n", max_i);
    }
    return 0;
}