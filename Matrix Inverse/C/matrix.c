#include <stdio.h>
int main()
{
    int a, b, c, d, test_case = 1;
    while (scanf("%d %d %d %d", &a, &b, &c, &d) == 4)
    {
        printf("Case %d:\n", test_case++);
        int det = a*d - b*c;
        printf("%d %d\n%d %d\n", d / det, -b / det, -c / det, a / det);
    }
    return 0;
}