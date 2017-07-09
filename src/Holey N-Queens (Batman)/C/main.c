#include <stdio.h>
#include <string.h>

int abs(int x)
{
    return x < 0 ? -x : x;
}

int attacks(int r1, int c1, int r2, int c2)
{
    return r1 == r2 || c1 == c2 || abs(r1 - r2) == abs(c1 - c2) ? 1 : 0;
}

int attacks_prior(int* vars, int next)
{
    for (int prev = 0; prev < next; prev++)
    {
        if (attacks(vars[next], next, vars[prev], prev)) return 1;
    }
    return 0;
}

int solve(int* vars, char* holes, int next, int n)
{
    if (next == n) return 1;

    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        vars[next] = i;
        if (holes[n * i + next]) continue;
        if (attacks_prior(vars, next)) continue;
        sum += solve(vars, holes, next + 1, n);
    }
    return sum;
}

int solutions(int n, char* holes)
{
    int variables[n]; // columns make up variables
    return solve(variables, holes, 0, n);
}

int main()
{
    int n,h;
    char holes[144];
    while(1)
    {
        scanf("%d %d", &n, &h);
        if (!n && !h) break;
        memset(holes, 0, 144 * sizeof(char));
        while(h--)
        {
            int r,c;
            scanf("%d %d", &r, &c);
            holes[r * n + c] = 1;
        }
        printf("%d\n", solutions(n, holes));
    }
    return 0;
}