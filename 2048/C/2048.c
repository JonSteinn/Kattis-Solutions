#include <stdio.h>
#include <stdlib.h>

short* init_board();
short get_number(short* board, int x, int y);
void set_number(short* board, int x, int y, short value);
void left(short* board);
void up(short* board);
void right(short* board);
void down(short* board);
void update(short* board);
void show(short* board);

int main()
{
    short* board = init_board();
    update(board);
    show(board);
    free(board);
    return 0;
}

// Read and store board in array
short* init_board()
{
    short* board = (short*)calloc(16,sizeof(short));
    int i;
    for (i = 3; i >=0; i--) {
        scanf("%hi %hi %hi %hi",
              board + (i << 2),
              board + (1 + (i << 2)),
              board + (2 + (i << 2)),
              board + (3 + (i << 2)));
    }
    return board;
}

short get_number(short* board, int x, int y)
{
    return *(board + ((y<<2)+x));
}

void set_number(short* board, int x, int y, short value)
{
    *(board + ((y<<2)+x)) = value;
}

void left(short* board)
{
    int x,y;
    for (y = 0; y < 4; y++)
    {
        for (x = 0; x < 3; x++)
        {
            int i, val, current = get_number(board, x, y);
            for (i = x + 1; i < 4; i++) if (val = get_number(board, i, y)) break;
            if (val == 0) break;
            if (current == 0) {
                set_number(board, x, y, val);
                set_number(board, i, y, 0);
                x--;
                continue;
            }
            else
            {
                if (val == current)
                {
                    set_number(board, x, y, current << 1);
                    set_number(board, i, y, 0);
                }
                else if (i > x + 1)
                {
                    set_number(board, x + 1, y, val);
                    set_number(board, i, y, 0);
                }
            }
        }
    }
}

void up(short* board)
{
    int x,y;
    for (x = 0; x < 4; x++)
    {
        for (y = 3; y > 0; y--)
        {
            int i, val, current = get_number(board, x, y);
            for (i = y - 1; i >= 0; i--) if (val = get_number(board, x, i)) break;
            if (val == 0) break;
            if (current == 0)
            {
                set_number(board, x, y, val);
                set_number(board, x, i, 0);
                y++;
                continue;
            }
            else
            {
                if (val == current)
                {
                    set_number(board, x, y, current << 1);
                    set_number(board, x, i, 0);
                }
                else if (i < y - 1)
                {
                    set_number(board, x, y - 1, val);
                    set_number(board, x, i, 0);
                }
            }
        }
    }
}

void right(short* board)
{
    int x,y;
    for (y = 0; y < 4; y++)
    {
        for (x = 3; x > 0; x--)
        {
            int i, val, current = get_number(board, x, y);
            for (i = x - 1; i >= 0; i--) if (val = get_number(board, i, y)) break;
            if (val == 0) break;
            if (current == 0)
            {
                set_number(board, x, y, val);
                set_number(board, i, y, 0);
                x++;
                continue;
            }
            else
            {
                if (val == current)
                {
                    set_number(board, x, y, current << 1);
                    set_number(board, i, y, 0);
                }
                else if (i < x - 1)
                {
                    set_number(board, x - 1, y, val);
                    set_number(board, i, y, 0);
                }
            }
        }
    }
}

void down(short* board)
{
    int x,y;
    for (x = 0; x < 4; x++)
    {
        for (y = 0; y < 3; y++)
        {
            int i, val, current = get_number(board, x, y);
            for (i = y + 1; i < 4; i++) if (val = get_number(board, x, i)) break;
            if (val == 0) break;
            if (current == 0)
            {
                set_number(board, x, y, val);
                set_number(board, x, i, 0);
                y--;
                continue;
            }
            else
            {
                if (val == current)
                {
                    set_number(board, x, y, current << 1);
                    set_number(board, x, i, 0);
                }
                else if (i > y + 1)
                {
                    set_number(board, x, y + 1, val);
                    set_number(board, x, i, 0);
                }
            }
        }
    }
}

void update(short* board)
{
    int n;
    scanf("%d",&n);
    if (n == 0) left(board);
    else if (n==1) up(board);
    else if (n==2) right(board);
    else down(board);
}

void show(short* board)
{
    int i;
    for (i = 3; i >= 0; i--) printf("%hi %hi %hi %hi\n",
                                    get_number(board, 0, i),
                                    get_number(board, 1, i),
                                    get_number(board, 2, i),
                                    get_number(board, 3, i));
}