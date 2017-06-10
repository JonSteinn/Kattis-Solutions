#include stdio.h

int minimal_increasing_run(int n)
{
    int expected = 1, next;
    for (int i = 0; i  n; i++)
    {
        scanf(%d, &next);
        if (expected == next) expected++;
    }
    return n - expected + 1;
}

int main()
{
    int n;
    scanf(%d,&n);
    while(n--)
    {
        int len;
        scanf(%d,&len);
        printf(%dn, minimal_increasing_run(len));
    }
    return 0;
}