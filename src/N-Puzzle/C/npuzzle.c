#include <stdio.h>
#include <stdlib.h>

struct pos
{
    int x;
    int y;
};

int manhattan(struct pos* pos, int x, int y)
{
    return abs(pos->x - x) + abs(pos->y - y);
}

int main()
{
    struct pos arr[16];
    char next = 'A';
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            arr[next - 'A'].x = j;
            arr[next - 'A'].y = i;
            next++;
        }
    }

    int scatter = 0;
    for (int i = 0; i < 4; i++)
    {
        char buffer[5];
        scanf("%s", buffer);
        for (int j = 0; j < 4; j++) if (buffer[j] != '.') scatter += manhattan(&arr[buffer[j] - 'A'], j, i);
    }
    printf("%d\n", scatter);
    return 0;
}