#include <stdio.h>

int getNext(int* a, int* b)
{
    scanf("%d %d", a, b);
    return *a || *b;
}

int main()
{
    int a, b;
    while (getNext(&a, &b)) printf("%d %d / %d\n", a / b, a % b, b);
    return 0;
}