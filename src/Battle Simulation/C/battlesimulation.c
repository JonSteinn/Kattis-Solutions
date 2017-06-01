#include <stdio.h>
#include <string.h>

#define BIT(x) ((x) == 'R' ? 1 : (x) == 'B' ? 2 : 4)

int main()
{
    char buffer[1000001];
    scanf("%s", buffer);
    size_t next = 0, len = strlen(buffer);
    while (next < len)
    {
        if (next + 2 < len && (BIT(buffer[next]) | BIT(buffer[next+1]) | BIT(buffer[next+2])) == 7)
        {
            printf("C");
            next += 3;
        }
        else
        {
            printf(buffer[next] == 'R' ? "S" : buffer[next] == 'B' ? "K" : "H");
            next++;
        }
    }
    printf("\n");
    return 0;
}