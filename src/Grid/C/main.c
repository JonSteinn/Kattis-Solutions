#include <stdio.h>
#include "point2D.h"

int main()
{
    short r, c;
    scanf("%hi %hi",&r,&c);
    char board[r][c];
    for (int i = 0; i < r; i++) scanf("%s",board[i]);

    int total = c * r;
    int* closed = (int*)calloc((size_t)total, sizeof(int));
    queue open;
    init(&open, total << 2);

    add(&open, 0, 0, 0);
    int goal_cost = -1;

    while (!is_empty(&open))
    {
        point* current = poll(&open);
        short curr_c = current->x;
        short curr_r = current->y;
        int curr_cost = current->cost;
        int one_dim = curr_r * c + curr_c;
        if (closed[one_dim]) continue;
        closed[one_dim] = 1;
        short val = (short)(board[curr_r][curr_c] - '0');


        // Up
        if (curr_r >= val && !closed[(curr_r - val) * c + curr_c])
        {
            add(&open, curr_c, curr_r - val, curr_cost + 1);
        }

        // Down
        if (curr_r < r - val && !closed[(curr_r + val) * c + curr_c])
        {
            if (curr_c == c - 1 && curr_r + val == r - 1)
            {
                goal_cost = curr_cost + 1;
                break;
            }
            else
            {
                add(&open, curr_c, curr_r + val, curr_cost + 1);
            }
        }

        // Left
        if (curr_c >= val && !closed[curr_r * c + curr_c - val])
        {
            add(&open, curr_c - val, curr_r, curr_cost + 1);
        }

        // Right
        if (curr_c < c - val && !closed[curr_r * c + curr_c + val])
        {
            if (curr_c + val == c - 1 && curr_r == r - 1)
            {
                goal_cost = curr_cost + 1;
                break;
            }
            else
            {
                add(&open, curr_c + val, curr_r, curr_cost + 1);
            }
        }
    }

    printf("%d\n", goal_cost);

    destroy(&open);
    free(closed);
    return 0;
}