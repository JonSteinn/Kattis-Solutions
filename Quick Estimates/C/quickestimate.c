#include <stdio.h>
#include <string.h>
int main()
{
    int n;
    scanf("%d", &n);
    while (n-- > 0)
    {
        char buffer[102];
        scanf("%s", buffer);
        printf("%d\n", strlen(buffer));
    }
}