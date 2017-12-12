#include <stdio.h>
#include <string.h>

int main()
{
    int battles = 0, counter = 0;
    char buffer[1001];
    scanf("%d", &battles);
    while(battles--)
    {
        scanf("%s", buffer);
        if (strstr(buffer, "CD") == NULL) counter++;
    }
    printf("%d\n", counter);
    return 0;
}