#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n-->0)
    {
        int k;
        scanf("%d",&k);
        printf("%d\n",(1<<k)-1);
    }
    return 0;
}