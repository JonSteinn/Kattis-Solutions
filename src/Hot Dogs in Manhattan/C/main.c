#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//*************************//
/* TODO: Cleanup & comment */
//*************************//

struct pos
{
    short r;
    short c;
};

struct extremes
{
    //struct pos ext[4]; // <-- TODO
    struct pos r_lo;
    struct pos r_hi;
    struct pos c_lo;
    struct pos c_hi;
};

int bfs(short* map, struct pos** stack_arr, struct pos** curr_arr, int r, int c, struct extremes* ex)
{
    int stack_id = 0;
    short one = 1;
    short cost = 0;
    while (stack_arr[0] != curr_arr[0] || stack_arr[1] != curr_arr[1])
    {
        int first = 1;
        while (stack_arr[stack_id] != curr_arr[stack_id])
        {
            curr_arr[stack_id]--;
            short curr_c = curr_arr[stack_id]->c;
            short curr_r = curr_arr[stack_id]->r;
            int one_dim = curr_r * c + curr_c;
            if (map[one_dim] < 0)
            {
                map[one_dim] = cost;
                if (cost > 0)
                {
                    if (first)
                    {
                        first = 0;
                        ex[cost].c_hi.c = curr_c;
                        ex[cost].c_lo.c = curr_c;
                        ex[cost].r_hi.c = curr_c;
                        ex[cost].r_lo.c = curr_c;
                        ex[cost].c_hi.r = curr_r;
                        ex[cost].c_lo.r = curr_r;
                        ex[cost].r_hi.r = curr_r;
                        ex[cost].r_lo.r = curr_r;
                    }
                    else
                    {
                        if (ex[cost].c_hi.c < curr_c)
                        {
                            ex[cost].c_hi.c = curr_c;
                            ex[cost].c_hi.r = curr_r;
                        }

                        if (ex[cost].c_lo.c > curr_c)
                        {
                            ex[cost].c_lo.c = curr_c;
                            ex[cost].c_lo.r = curr_r;
                        }

                        if (ex[cost].r_hi.r < curr_r)
                        {
                            ex[cost].r_hi.c = curr_c;
                            ex[cost].r_hi.r = curr_r;
                        }

                        if (ex[cost].r_lo.r > curr_r)
                        {
                            ex[cost].r_lo.c = curr_c;
                            ex[cost].r_lo.r = curr_r;
                        }
                    }
                }
                if (curr_r > 0 && map[(curr_r - 1) * c + curr_c] < 0)
                {
                    curr_arr[!stack_id]->r = curr_r - one;
                    curr_arr[!stack_id]->c = curr_c;
                    curr_arr[!stack_id]++;
                }
                if (curr_r < r - 1 && map[(curr_r + 1) * c + curr_c] < 0)
                {
                    curr_arr[!stack_id]->r = curr_r + one;
                    curr_arr[!stack_id]->c = curr_c;
                    curr_arr[!stack_id]++;
                }
                if (curr_c > 0 && map[curr_r * c + curr_c - 1] < 0)
                {
                    curr_arr[!stack_id]->r = curr_r;
                    curr_arr[!stack_id]->c = curr_c - one;
                    curr_arr[!stack_id]++;
                }
                if (curr_c < c - 1 && map[curr_r * c + curr_c + 1] < 0)
                {
                    curr_arr[!stack_id]->r = curr_r;
                    curr_arr[!stack_id]->c = curr_c + one;
                    curr_arr[!stack_id]++;
                }
            }
        }
        stack_id = !stack_id;
        cost++;
    }
    return cost - 1;
}

// for DEBUGGING
void print_map(short* map, int c, int r)
{
    for (int i = 0; i < c<<1; i++) printf("-");
    printf("\n");
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%hd ", map[i * c + j]);
        }
        printf("\n");
    }
    for (int i = 0; i < c<<1; i++) printf("-");
    printf("\n");
}

int manhattan_distance(struct pos* a, struct pos* b)
{
    int r = a->r - b->r;
    int c = a->c - b->c;
    return (r < 0 ? -r : r) + (c < 0 ? -c : c);
}

// TODO: change data structure to array and iterate instead of repeating...
int max_for_dist(struct extremes* ex, int supreme)
{
    int upper = 0;
    int x = manhattan_distance(&ex->r_hi, &ex->r_lo);
    if (upper < x)
    {
        if (x >= supreme) return supreme;
        upper = x;
    }
    x = manhattan_distance(&ex->r_hi, &ex->c_hi);
    if (upper < x)
    {
        if (x >= supreme) return supreme;
        upper = x;
    }
    x = manhattan_distance(&ex->r_hi, &ex->c_lo);
    if (upper < x)
    {
        if (x >= supreme) return supreme;
        upper = x;
    }
    x = manhattan_distance(&ex->r_lo, &ex->c_hi);
    if (upper < x)
    {
        if (x >= supreme) return supreme;
        upper = x;
    }
    x = manhattan_distance(&ex->r_lo, &ex->c_lo);
    if (upper < x)
    {
        if (x >= supreme) return supreme;
        upper = x;
    }
    x = manhattan_distance(&ex->c_hi, &ex->c_lo);
    if (upper < x) upper = x > supreme ? supreme : x;
    return upper;
}

int max_distance(int max_possible, struct extremes* ex)
{
    int current_max = 0;
    while(max_possible > current_max)
    {
        int x = max_for_dist(&ex[max_possible], max_possible);
        if (x > current_max) current_max = x;
        max_possible--;
    }
    return current_max;
}

int main()
{
    int tc;
    scanf("%d", &tc);
    struct extremes ex[2000];
    short map[1000000];
    struct pos* stack_arr[2];
    stack_arr[0] = (struct pos*)malloc(sizeof(struct pos) * 8000000);
    stack_arr[1] = stack_arr[0] + 4000000;
    while(tc--)
    {
        short n, c, r;
        scanf("%hd %hd %hd", &n, &c, &r);
        if (!n) printf("%d\n", c + r - 2);
        else
        {
            memset(ex, 0, sizeof(ex));
            memset(map, -1, sizeof(map));
            struct pos* curr_arr[2];
            curr_arr[0] = stack_arr[0];
            curr_arr[1] = stack_arr[1];

            for (int i = 0; i < n; i++)
            {
                short x,y;
                scanf("%hd %hd", &x, &y);
                curr_arr[0]->r = y;
                curr_arr[0]->c =x;
                curr_arr[0]++;
            }
            int max_cost = bfs(map, stack_arr, curr_arr, r, c, ex);
            //print_map(map, c, r); // DEBUGGING
            printf("%d\n", max_distance(max_cost, ex));
        }
    }
    free(stack_arr[0]);
    return 0;
}