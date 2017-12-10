#include <stdio.h>

void test_case()
{
    int r, e, c;
    scanf("%d %d %d", &r, &e, &c);
    int d = r - (e - c);
    printf(d < 0 ? "advertise\n" : d > 0 ? "do not advertise\n" : "does not matter\n");
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
}