#include <stdio.h>
#define SINGULAR "piece"
#define PLURAL "pieces"
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    int diff = a - b;
    if (a < b) printf("Dr. Chaz will have %d %s of chicken left over!", -diff, diff == -1 ? SINGULAR : PLURAL);
    else printf("Dr. Chaz needs %d more %s of chicken!", diff, diff == 1 ? SINGULAR : PLURAL);
    return 0;
}