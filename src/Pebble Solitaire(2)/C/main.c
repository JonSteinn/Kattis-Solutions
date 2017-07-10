#include <stdio.h>
#include <string.h>
#include "Stack.h"

#define STATE_SPACE 8388608
#define TOTAL_CAVITIES 23

int pebbles_left(int state)
{
    state = state - ((state >> 1) & 0x55555555);
    state = (state & 0x33333333) + ((state >> 2) & 0x33333333);
    return (((state + (state >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
}

void set_bit(int* x, int b)
{
    *x |= (1 << b);
}

void unset_bit(int* x, int b)
{
    *x &= ~(1 << b);
}

int is_set(int x, int b)
{
    return x & (1 << b);
}

void add(int* set, int x)
{
    int d = x >> 5;
    set_bit(set + d, x - (d << 5));
}

int contains(int* set, int x)
{
    int d = x >> 5;
    return is_set(set[d], x - (d << 5));
}

void add_neighbors(stack* open, int* closed, int state)
{
    for (int i = 0; i < TOTAL_CAVITIES - 1; i++)
    {
        if (is_set(state, i) && is_set(state, i + 1))
        {
            if (i != 0 && !is_set(state, i - 1))
            {
                int n = state;
                unset_bit(&n, i);
                unset_bit(&n, i+1);
                set_bit(&n, i-1);
                if (!contains(closed, n)) push(open, n);
            }
            if (i != TOTAL_CAVITIES - 2 && !is_set(state, i + 2))
            {
                int n = state;
                unset_bit(&n, i);
                unset_bit(&n, i+1);
                set_bit(&n, i+2);
                if (!contains(closed, n)) push(open, n);
            }
        }
    }
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int solve(stack* open, int* closed)
{
    int least = TOTAL_CAVITIES;
    while(!is_empty(open))
    {
        int current = pop(open);
        if (contains(closed, current)) continue;
        add(closed, current);
        least = min(least, pebbles_left(current));
        if (least == 1) break;
        add_neighbors(open, closed, current);
    }
    return least;
}

int state_to_number(char* str)
{
    int x = 0;
    for (int i = 0; i < TOTAL_CAVITIES; i++)
    {
        if (str[i] == 'o') x |= (1 << i);
    }
    return x;
}

int main()
{
    int n;
    scanf("%d",&n);
    stack open;
    init(&open, STATE_SPACE);
    int closed[STATE_SPACE >> 5];
    while(n--)
    {
        char buffer[TOTAL_CAVITIES + 1];
        scanf("%s",buffer);
        memset(closed, 0, (STATE_SPACE >> 5) * sizeof(char));
        clear(&open);
        push(&open, state_to_number(buffer));
        printf("%d\n", solve(&open, closed));
    }
    destroy(&open);
    return 0;
}