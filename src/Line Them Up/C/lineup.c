#include <stdio.h>
#include <string.h>
int main()
{
    int n;
    scanf("%d", &n);
    char buffer[2][13];
    scanf("%s", buffer[0]);
    char flags = 0;
    int i;
    for (i = 1; i < n; i++)
    {
        scanf("%s", buffer[i&1]);
        flags |= (1 << (i&1 ? (strcmp(buffer[0], buffer[1]) < 0) : (strcmp(buffer[0], buffer[1]) > 0)));
    }
    printf(flags == 3 ? "NEITHER\n" : flags == 1 ? "DECREASING\n" : "INCREASING\n");
    return 0;
}