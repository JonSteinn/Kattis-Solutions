#include <stdio.h>
#include <string.h>

struct pos
{
    int x, y;
};

struct boundaries
{
    int max_y;
    int min_y;
    int max_x;
    int min_x;
};

void read_path(struct pos* path, int* len, struct boundaries* b)
{
    char buffer[5];
    while(scanf("%s",buffer) != EOF)
    {
        if (buffer[0] == 'u')
        {
            path[*len].x = path[(*len)-1].x;
            path[*len].y = path[(*len)-1].y + 1;
            if (path[*len].y > b->max_y) b->max_y = path[*len].y;
        }
        else if (buffer[0] == 'd')
        {
            path[*len].x = path[(*len)-1].x;
            path[*len].y = path[(*len)-1].y - 1;
            if (path[*len].y < b->min_y) b->min_y = path[*len].y;
        }
        else if (buffer[0] == 'r')
        {
            path[*len].x = path[(*len)-1].x + 1;
            path[*len].y = path[(*len)-1].y;
            if (path[*len].x > b->max_x) b->max_x = path[*len].x;
        }
        else
        {
            path[*len].x = path[(*len)-1].x - 1;
            path[*len].y = path[(*len)-1].y ;
            if (path[*len].x < b->min_x) b->min_x = path[*len].x;
        }
        (*len)++;
    }
}

int main()
{
    int len = 1;
    struct boundaries b;
    b.min_x = 0; b.min_y = 0; b.max_x = 0; b.max_y = 0;
    struct pos path[501];
    path[0].x = 0;
    path[0].y = 0;
    read_path(path, &len, &b);

    int w = b.max_x - b.min_x + 4; // + 1 for numbers on interval, + 2 for frame, + 1 for terminating null
    int h = b.max_y - b.min_y + 3; // + 1 for numbers on interval, + 2 for frame
    char output[h][w];
    for (int i = 0; i < h; i++) memset(output[i], ' ', (size_t)w);

    for (int i = 0; i < w - 1; i++)
    {
        output[0][i] = '#';
        output[h - 1][i] = '#';
    }
    for (int i = 0; i < h; i++)
    {
        output[i][0] = '#';
        output[i][w - 2] = '#';
        output[i][w - 1] = '\0';
    }

    for (int i = 1; i < len - 1; i++) output[b.max_y - path[i].y + 1][path[i].x - b.min_x + 1] = '*';
    output[b.max_y - path[0].y + 1][path[0].x - b.min_x + 1] = 'S';
    output[b.max_y - path[len-1].y + 1][path[len-1].x - b.min_x + 1] = 'E';

    for (int i = 0; i < h; i++)
    {
        printf("%s\n", output[i]);
    }

    return 0;
}
