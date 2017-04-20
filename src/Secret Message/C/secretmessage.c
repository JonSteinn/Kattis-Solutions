#include "stdio.h"
#include "math.h"
#include "string.h"

int next_square(int n)
{
    return (int)ceil(sqrt(n));
}

char get(char* str, int max, int width, int x, int y)
{
    int index = y * width + x;
    if (index >= max) return '*';
    return *(str + index);
}

void experiment()
{
    char buffer[10001];
    scanf("%s", buffer);
    int s_len = strlen(buffer);
    int width = next_square(s_len);
    int i, j;
    for (i = 0; i < width; i++)
    {
        for (j = width - 1; j >=0; j--)
        {
            char next = get(buffer, s_len, width, i, j);
            if (next != '*')
            {
                printf("%c", next);
            }
        }
    }
    printf("\n");
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n-- > 0) experiment();
    return 0;
}

/*
 * OsoT vtnh eite rseC
*/