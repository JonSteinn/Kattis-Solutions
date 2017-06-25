#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    unsigned long long half = (unsigned long long)(n>>1);
    printf("%llu\n", n&1 ? (half+1)*(half+2) : (half+1)*(half+1));
    return 0;
}