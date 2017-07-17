#include <stdio.h>
#include "BFS_Queue.h"
#include "Visited.h"

short one = 1;

struct parameters
{
    int x;
    int y;
    int t;
    int l;
    int w;
};

void add_point(int x, int y, struct parameters* p, visited* closed)
{
    visited_set(closed, y * p->x + x);
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int max(int a, int b)
{
    return a > b ? a : b;
}

void mark_walls(int* arr, struct parameters* p, visited* closed)
{
    arr[0]--; arr[1]--; arr[2]--; arr[3]--;
    if (arr[0] == arr[2]) // x1 == x2
    {
        int lo = min(arr[1], arr[3]);
        int hi = max(arr[1], arr[3]);
        for (int y = lo; y <= hi; y++) add_point(arr[0], y, p, closed);
    }
    else if (arr[1] == arr[3]) // y1 == y2
    {
        int lo = min(arr[0], arr[2]);
        int hi = max(arr[0], arr[2]);
        for (int x = lo; x <= hi; x++) add_point(x, arr[1], p, closed);
    }
    else if (arr[3]-arr[2] == arr[1] - arr[0])
    {
        if (arr[1] < arr[3])
        {
            for (int x = arr[0], y = arr[1]; x <= arr[2] && y <= arr[3]; x++, y++) add_point(x, y, p, closed);
        }
        else
        {
            for (int x = arr[2], y = arr[3]; x <= arr[0] && y <= arr[1]; x++, y++) add_point(x, y, p, closed);
        }
    }
    else
    {
        if (arr[1] > arr[3])
        {
            for (int x = arr[0], y = arr[1]; x <= arr[2] && y >= arr[3]; x++, y--) add_point(x, y, p, closed);
        }
        else
        {
            for (int x = arr[2], y = arr[3]; x <= arr[0] && y >= arr[1]; x++, y--) add_point(x, y, p, closed);
        }
    }
}

void iteration(queue* open, visited* closed, struct parameters* p, int* sum, int it)
{
    queue* from = &open[it];
    queue* to = &open[!it];

    while (!queue_is_empty(from))
    {
        pos* curr = queue_poll(from);
        short x = curr->x;
        short y = curr->y;
        int one_dim = y * p->x + x;
        if (visited_is_set(closed, one_dim)) continue;
        visited_set(closed, one_dim);
        (*sum)++;
        if (curr->x > 0 && !visited_is_set(closed, y * p->x + (x - 1))) queue_add(to, x - one, y);
        if (curr->x < p->x - 1 && !visited_is_set(closed, y * p->x + (x + 1))) queue_add(to, x + one, y);
        if (curr->y > 0 && !visited_is_set(closed, (y - 1) * p->x + x)) queue_add(to, x, y - one);
        if (curr->y < p->y - 1 && !visited_is_set(closed, (y + 1) * p->x + x)) queue_add(to, x, y + one);
    }
}

int covered(queue* open, visited* closed, struct parameters* p)
{
    for (int i = 0; i < p->l; i++)
    {
        short x, y;
        scanf("%hd %hd", &x, &y);
        queue_add(&open[0], x - one, y - one);
    }
    for (int i = 0; i < p->w; i++)
    {
        int arr[4];
        scanf("%d %d %d %d", arr, arr+1, arr+2, arr+3);
        mark_walls(arr, p, closed);
    }
    int covered_counter = 0;
    int total = p->x * p->y - p->w;
    for (int i = 0; i < p->t; i++)
    {
        iteration(open, closed, p, &covered_counter, i&1);
        if (covered_counter == total) break;
    }
    return covered_counter;
}

int main()
{
    queue open[2];
    visited closed;
    queue_init(&open[0], 8000000);
    queue_init(&open[1], 8000000);
    visited_init(&closed, 1000000);
    struct parameters p;
    while (1)
    {
        scanf("%d", &p.x);
        if (p.x < 0) break;
        scanf("%d %d %d %d", &p.y, &p.t, &p.l, &p.w);
        visited_unset_all(&closed);
        queue_reset(&open[0]);
        queue_reset(&open[1]);
        printf("%d\n", covered(open, &closed, &p));
    }

    queue_destroy(&open[0]);
    queue_destroy(&open[1]);
    visited_destroy(&closed);

    return 0;
}