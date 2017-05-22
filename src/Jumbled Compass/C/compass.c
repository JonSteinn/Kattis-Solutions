#include <stdio.h>

int main()
{
    int from, to;
    scanf("%d %d",&from,&to);
    if (from == to)
    {
        printf("0\n");
    }
    else if (from < to)
    {
        int dif1 = to - from;
        int dif2 = (360 - to) + from;
        if (dif1 <= dif2)
        {
            printf("%d\n",dif1);
        }
        else
        {
            printf("%d\n",-dif2);
        }
    }
    else // to < from
    {
        int dif1 = from - to;
        int dif2 = (360 - from) + to;
        if (dif1 < dif2)
        {
            printf("%d\n",-dif1);
        }
        else
        {
            printf("%d\n",dif2);
        }
    }
    return 0;
}