#include <stdio.h>

void test_case()
{
    int kids;
    scanf("%d",&kids);
    long long sum = 0;
    for (int i = 0; i < kids; i++)
    {
        long long temp;
        scanf("%lld",&temp);
        sum += temp;
        if (sum > kids) sum %= kids;
    }
    printf(sum == 0 || sum == kids ? "YES\n" : "NO\n");
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}