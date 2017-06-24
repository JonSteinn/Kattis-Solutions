#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct position
{
    int x;
    int y;
};
typedef struct position pos;

int comparator(const void* a, const void* b)
{
    pos* _a = (pos*)a;
    pos* _b = (pos*)b;
    int y = _a->y - _b->y;
    return y ? y : _a->x - _b->x;
}

int invalid(char* msg, size_t size)
{
    for (int i = 0; i < size; i++)
    {
        if (!msg[i]) return 1;
    }
    return 0;
}

int main()
{
    int w;
    scanf("%d",&w);
    size_t w_sq = (size_t)(w * w);
    size_t grille_size = 0;
    char board[w][w + 1];

    for (int i = 0; i < w; i++)
    {
        scanf("%s", board[i]);
        for (int j = 0; j < w; j++)
        {
            if (board[i][j] == '.') grille_size++;
        }
    }

    int index = 0;
    pos grille[grille_size];
    for (int i = 0; i < w; i++) {
        for (int j = 0; j < w; j++) {
            if (board[i][j] == '.')
            {
                grille[index].x = j;
                grille[index].y = i;
                index++;
            }
        }
    }

    index = 0;
    char msg[w_sq + 1];
    scanf("%s",msg);

    char msg_out[w_sq + 1];
    memset(msg_out, 0, w_sq + 1);

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < grille_size; j++)
        {
            int one_dim = grille[j].y * w + grille[j].x;
            msg_out[one_dim] = msg[index++];
            int tmp = grille[j].x;
            grille[j].x = w - 1 - grille[j].y;
            grille[j].y = tmp;
        }
        if (i < 3) qsort(grille, grille_size, sizeof(pos), comparator);
    }

    if (invalid(msg_out, w_sq)) printf("invalid grille\n");
    else printf("%s\n", msg_out);

    return 0;
}