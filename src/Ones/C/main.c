#include stdio.h

int main()
{
    int n;
    while (scanf(%d,&n) == 1)
    {
        int counter = 0;
        int remainder = 1;
        while (remainder % n)
        {
            remainder = (10  remainder + 1) % n;
            counter++;
        }
        printf(%dn,counter + 1);
    }
    return 0;
}