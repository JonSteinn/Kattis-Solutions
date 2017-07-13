#include <stdio.h>

int first(int* current, int cap)
{
    int a, b, c;
    scanf("%d %d %d",&a,&b,&c);
    *current += b;
    return !a && b <= cap && (!c || b == cap);
}

int next(int* current, int cap)
{
    int a, b, c;
    scanf("%d %d %d",&a,&b,&c);
    if (a > *current) return 0;
    *current -= a;
    if (*current + b > cap) return 0;
    *current += b;
    if (c > 0 && *current != cap) return 0;
}

int last(int* current)
{
    int a, b, c;
    scanf("%d %d %d",&a,&b,&c);
    return a == *current && !b && !c;
}

void dump(int n)
{
    int a, b, c;
    while(n--) scanf("%d %d %d", &a, &b, &c);
}

int main()
{
    int c, n;
    scanf("%d %d",&c,&n);

    int possible = 1;
    int current = 0;
    if (!(possible = first(&current, c))) dump(n-1);

    for (int i = 1; i < n - 1; i++)
    {
        if (!(possible = next(&current, c)))
        {
            dump(n - i - 1);
            break;
        }
    }

    if (possible) possible = last(&current);

    printf(possible ? "possible\n" : "impossible\n");


    return 0;
}