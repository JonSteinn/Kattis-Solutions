#include <stdio.h>
int main()
{
    int h, m;
    scanf("%d %d", &h, &m);
    printf("%d %d\n", m/60, (m = ((m+60*h-45)+1440)%1440)%60);
    return 0;
}