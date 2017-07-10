#include <stdio.h>
#include <string.h>
#include "stack.h"

char one = 1;

void spread(char* mat, stack* open, char* closed, stack* colors, char val, int n, char* origin)
{
    int index = val - '1';
    while(!empty(open))
    {
        pos* curr = pop(open);
        char curr_r = curr->r, curr_c = curr->c;
        int one_dim = curr_r * (n + 1) + curr_c;
        if (origin[one_dim] || closed[one_dim] || mat[one_dim] != val) continue;
        closed[one_dim] = 1;
        push(&colors[index], curr_r, curr_c);

        if (curr_r > 0)
        {
            int dim1 = (curr_r - 1) * (n + 1) + curr_c;
            if (!origin[dim1] && !closed[dim1] && mat[dim1] == val) push(open, curr_r - one, curr_c);
        }
        if (curr_r < n - 1)
        {
            int dim1 = (curr_r + 1) * (n + 1) + curr_c;
            if (!origin[dim1] && !closed[dim1] && mat[dim1] == val) push(open, curr_r + one, curr_c);
        }
        if (curr_c > 0)
        {
            int dim1 = curr_r * (n + 1) + curr_c - 1;
            if (!origin[dim1] && !closed[dim1] && mat[dim1] == val) push(open, curr_r, curr_c - one);
        }
        if (curr_c < n - 1)
        {
            int dim1 = curr_r * (n + 1) + curr_c + 1;
            if (!origin[dim1] && !closed[dim1] && mat[dim1] == val) push(open, curr_r, curr_c + one);
        }
    }
}

void fill_init(char* mat, stack* colors, char* closed, stack* open, int n, char* n_closed, stack* dfs_open)
{
    while (!empty(open))
    {
        pos* p = pop(open);
        char curr_r = p->r, curr_c = p->c;
        int one_dim = curr_r * (n + 1) + curr_c;
        if (closed[one_dim]) continue;
        char val = mat[one_dim];
        if (val == mat[0])
        {
            closed[one_dim] = 1;
            if (curr_r > 0 && !closed[(curr_r - 1) * (n + 1) + curr_c]) push(open, curr_r - one, curr_c);
            if (curr_r < n - 1 && !closed[(curr_r + 1) * (n + 1) + curr_c]) push(open, curr_r + one, curr_c);
            if (curr_c > 0 && !closed[curr_r * (n + 1) + curr_c - 1]) push(open, curr_r, curr_c - one);
            if (curr_c < n - 1 && !closed[curr_r * (n + 1) + curr_c + 1]) push(open, curr_r, curr_c + one);
        }
        else
        {
            if (!n_closed[one_dim])
            {
                clear(dfs_open);
                push(dfs_open, curr_r, curr_c);
                spread(mat, dfs_open, n_closed, colors, val, n, closed);
            }
        }
    }
}

void next_move(char* mat, stack* colors, char* closed, int n, char* n_closed, int max, stack* dfs_open)
{
    stack* from = &colors[max];
    while(!empty(from))
    {
        pos* curr = pop(from);
        char curr_r = curr->r, curr_c = curr->c;
        int one_dim = curr_r * (n + 1) + curr_c;

        if (closed[one_dim]) continue;
        closed[one_dim] = 1;

        if (curr_r > 0)
        {
            int above = (curr_r - 1) * (n + 1) + curr_c;
            if (!closed[above] && !n_closed[above])
            {
                clear(dfs_open);
                push(dfs_open, curr_r - one, curr_c);
                spread(mat, dfs_open, n_closed, colors, mat[above], n, closed);
            }
        }
        if (curr_r < n - 1)
        {
            int below = (curr_r + 1) * (n + 1) + curr_c;
            if (!closed[below] && !n_closed[below])
            {
                clear(dfs_open);
                push(dfs_open, curr_r + one, curr_c);
                spread(mat, dfs_open, n_closed, colors, mat[below], n, closed);
            }
        }
        if (curr_c > 0)
        {
            int left = curr_r * (n + 1) + curr_c - 1;
            if (!closed[left] && !n_closed[left])
            {
                clear(dfs_open);
                push(dfs_open, curr_r, curr_c - one);
                spread(mat, dfs_open, n_closed, colors, mat[left], n, closed);
            }
        }
        if (curr_c < n - 1)
        {
            int right = curr_r * (n + 1) + curr_c + 1;
            if (!closed[right] && !n_closed[right])
            {
                clear(dfs_open);
                push(dfs_open, curr_r, curr_c + one);
                spread(mat, dfs_open, n_closed, colors, mat[right], n, closed);
            }
        }
    }
}

int most(stack* colors)
{
    int max = 0;
    for (int i = 1; i < 6; i++)
    {
        if (colors[max].count < colors[i].count) max = i;
    }
    return max;
}

int remaining(stack* c)
{
    int s = 0;
    for (int i = 0; i < 6; i++) s += c[i].count;
    return s;
}

void test_case(char* mat, stack* colors, char* closed, stack* init_open, char* n_closed, stack* dfs_open)
{
    int n;
    scanf("%d",&n);
    for (int i = 0; i < n; i++) scanf("%s", mat + i * (n + 1));

    push(init_open, 0, 0);
    fill_init(mat, colors, closed, init_open, n, n_closed, dfs_open);

    int moves = 0;
    int used[6] = {0,0,0,0,0,0};
    while (remaining(colors) > 0)
    {
        int m = most(colors);
        used[m]++;
        next_move(mat, colors, closed, n, n_closed, m, dfs_open);
        moves++;
    }

    printf("%d\n", moves);
    printf("%d %d %d %d %d %d\n", used[0], used[1], used[2], used[3], used[4], used[5]);
}

int main()
{
    char arr[1260];
    char* set = arr;
    char* neighbors_set = arr + 420;
    char* mat = arr + 840;

    stack colors[6];
    for (int i = 0; i < 6; i++) init(colors + i, 1600);
    stack init_dfs_open, dfs_open;
    init(&init_dfs_open, 1600);
    init(&dfs_open, 1600);

    int n;
    scanf("%d",&n);
    while(n--)
    {
        memset(arr, 0, 840 * sizeof(char));
        for (int i = 0; i < 6; i++) clear(colors + i);
        clear(&init_dfs_open);
        test_case(mat, colors, set, &init_dfs_open, neighbors_set, &dfs_open);
    }

    for (int i = 0; i < 6; i++) destroy(colors + i);
    destroy(&init_dfs_open);

    return 0;
}