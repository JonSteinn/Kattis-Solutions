#include <stdio.h>
#include <string.h>

int main()
{
    int x = 0, y = 0;
    char buffer[31];
    scanf("%s", buffer);
    int level = (int)strlen(buffer);
    int i;
    for (i = 0; i < level; i++)
    {
        if (buffer[i] == '1' || buffer[i] == '3') x += (1 << level) >> (i + 1);
        if (buffer[i] == '2' || buffer[i] == '3') y += (1 << level) >> (i + 1);
    }
    printf("%d %d %d\n", level, x, y);
    return 0;
}