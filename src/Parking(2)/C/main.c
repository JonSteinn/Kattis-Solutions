#include stdio.h

int main()
{
    int n;
    scanf(%d,&n);
    while(n--)
    {
        int s;
        scanf(%d,&s);
        int min = 99, max = 0;
        while(s--)
        {
            int m;
            scanf(%d,&m);
            if (min  m) min = m;
            if (max  m) max = m;
        }
        printf(%dn, (max-min)1);
    }
    return 0;
}