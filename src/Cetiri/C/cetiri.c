#include <stdio.h>

void swap(int* a, int* b)
{
    *a^=*b^=*a^=*b;
}

void three_sort(int* a, int* b, int* c)
{
    if (*a > *b) swap(a, b);
    if (*a > *c) swap(a, c);
    if (*b > *c) swap(b, c);
}

int missing(int a, int b, int c)
{
    three_sort(&a,&b,&c);
    return b-a == c-b ? c+b-a : (c-(b+b-a)) == b-a ? c-(b-a) : a+c-b;
}

int main()
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("%d\n", missing(a,b,c));
}