#include <stdio.h>

/*
 * Assume a >= b.
 * a + b = s AND a - b = d => 2a = s+d => a = (s+d)/2
 * a - b = d AND a = (s+d)/2 => b = a - d
 */

void test_case()
{
    int s, d;
    scanf("%d %d",&s,&d);
    int a = (s+d)/2;
    int b = a - d;
    if (a*2 == s+d && b >= 0) printf("%d %d\n", a, b);
    else printf("impossible\n");
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}