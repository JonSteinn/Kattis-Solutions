#include <stdio.h>
#include <math.h>

int _binomial[11][11];

int binomial(int n, int k)
{
    return k < 0 || k > n ? 0 : _binomial[n][k];

}

void set_binomial()
{
    _binomial[0][0] = 1;
    for (int n = 1; n < 11; n++)
    {
        for (int k = 0; k <= n; k++)
        {
            _binomial[n][k] = binomial(n - 1, k - 1) + binomial(n - 1, k);
        }
    }
}

void test_case()
{
    int r,s,x,y,w;
    scanf("%d %d %d %d %d",&r,&s,&x,&y,&w);
    double above_or_eq = (s - r + 1.0) / s, below = (1 - above_or_eq), p_win = 0, p_lose = 0;
    for (int i = x; i <= y; i++) p_win += binomial(y, i) * pow(above_or_eq, i) * pow(below, y - i);
    p_lose = 1 - p_win;
    printf(p_win * (w - 1) + p_lose * (-1) > 0 ? "yes\n" : "no\n");
}

int main()
{
    set_binomial();
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}