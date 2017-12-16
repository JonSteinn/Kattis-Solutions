#include <stdio.h>
#include <string.h>

#define MOD 1001113

typedef unsigned long long ull;

ull mem[10201];

ull permutations(int N, int v)
{
    int index  = N * 101 + v;
    if (v == 0 || v == N - 1) mem[index] = 1;
    if (!mem[index]) mem[index] = ((v + 1) * permutations(N - 1, v) + (N - v) * permutations(N - 1, v - 1)) % MOD;
    return mem[index];
}

int main()
{
    memset(mem, 0, sizeof(mem));
    mem[102] = 1;
    int n;
    scanf("%d", &n);
    while(n--)
    {
        int k, N, v;
        scanf("%d %d %d", &k, &N, &v);
        printf("%d %llu\n", k, permutations(N, v));
    }
    return 0;
}