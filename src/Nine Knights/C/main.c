#include <stdio.h>

#define KNIGHT 'k'

typedef struct {
    int x, y;
} pos;

int is_valid(pos* arr, int count, int set)
{
    if (count != 9) return 0;
    for (int i = 0; i < count; i++)
    {
        if (arr[i].x - 2 >= 0)
        {
            if (arr[i].y - 1 >= 0 && set & (1 << ((arr[i].y - 1) * 5 + arr[i].x - 2))) return 0;
            if (arr[i].y + 1 < 5 && set & (1 << ((arr[i].y + 1) * 5 + arr[i].x - 2))) return 0;
        }
        if (arr[i].x + 2 < 5)
        {
            if (arr[i].y - 1 >= 0 && set & (1 << ((arr[i].y - 1) * 5 + arr[i].x + 2))) return 0;
            if (arr[i].y + 1 < 5 && set & (1 << ((arr[i].y + 1) * 5 + arr[i].x + 2))) return 0;
        }
        if (arr[i].y - 2 >= 0)
        {
            if (arr[i].x - 1 >= 0 && set & (1 << ((arr[i].y - 2) * 5 + arr[i].x - 1))) return 0;
            if (arr[i].x + 1 < 5 && set & (1 << ((arr[i].y - 2) * 5 + arr[i].x + 1))) return 0;
        }
        if (arr[i].y + 2 < 5)
        {
            if (arr[i].x - 1 >= 0 && set & (1 << ((arr[i].y + 2) * 5 + arr[i].x - 1))) return 0;
            if (arr[i].x + 1 < 5 && set & (1 << ((arr[i].y + 2) * 5 + arr[i].x + 1))) return 0;
        }
    }

    return 1;
}

int main()
{
    pos positions[25];
    int count = 0;
    char buffer[6];
    int set = 0;
    for (int i = 0; i < 5; i++)
    {
        scanf("%s", buffer);
        for (int j = 0; j < 5; j++)
        {
            if (buffer[j] == KNIGHT)
            {
                positions[count].y = i;
                positions[count].x = j;
                count++;

                set |= (1 << (i * 5 + j));
            }
        }
    }

    printf(is_valid(positions, count, set) ? "valid\n" : "invalid\n");

    return 0;
}