#include <stdio.h>
#include "point2D.h"

#define UNUSED(x) (void)(x)

int main()
{
    int r,c;
    UNUSED(scanf("%d %d",&r,&c));

    char map[r][c+1];
    for (int i = 0; i < r; i++) UNUSED(scanf("%s", map[i]));

    int total = r * c;
    int next_group = 1;
    int *group = (int*)calloc((size_t)total, sizeof(int));
    short one = 1;

    stack open;
    init(&open, total<<2);

    int q;
    UNUSED(scanf("%d",&q));

    while (q--)
    {
        short r1,c1,r2,c2;
        UNUSED(scanf("%hi %hi %hi %hi",&r1,&c1,&r2,&c2));
        r1--; c1--; r2--; c2--;
        int dim_one_1 = r1 * c + c1;
        int dim_one_2 = r2 * c + c2;

        if (dim_one_1 == dim_one_2) printf(map[r1][c1] == '1' ? "decimal\n" : "binary\n");
        else if (group[dim_one_1] == 0 && group[dim_one_2] == 0)
        {
            // DFS
            push(&open, r1, c1);
            while (!is_empty(&open))
            {
                point* curr = pop(&open);
                short curr_x = curr->x, curr_y = curr->y;
                char curr_val = map[curr_x][curr_y];
                int dim_one = curr_x * c + curr_y;
                if (group[dim_one]) continue;
                group[dim_one] = next_group;
                if (curr_x > 0 && map[curr_x-1][curr_y] == curr_val && !group[(curr_x-1)*c+curr_y]) push(&open, curr_x-one, curr_y);
                if (curr_x < r - 1 && map[curr_x+1][curr_y] == curr_val && !group[(curr_x+1)*c+curr_y]) push(&open, curr_x+one, curr_y);
                if (curr_y > 0 && map[curr_x][curr_y-1] == curr_val && !group[curr_x*c+curr_y-1]) push(&open, curr_x, curr_y-one);
                if (curr_y < c - 1 && map[curr_x][curr_y+1] == curr_val && !group[curr_x*c+curr_y+1]) push(&open, curr_x, curr_y+one);
            }
            next_group++;
            printf(group[dim_one_2] ? (map[r1][c1] == '1' ? "decimal\n" : "binary\n") : ("neither\n"));
        }
        else if (map[r1][c1] != map[r2][c2]) printf("neither\n");
        else if (group[dim_one_1] == group[dim_one_2]) printf(map[r1][c1] == '1' ? "decimal\n" : "binary\n");
        else printf("neither\n");
    }

    destroy(&open);
    free(group);

    return 0;
}