#include <stdio.h>

int next_power_of_two(int n)
{
    n--;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    return ++n;
}

int breaks_needed(int bar, int squares)
{
    int count = 0;
    while (squares > 0 && squares != bar)
    {
        bar >>= 1;
        if (squares > bar) {
            squares -= bar;
        }
        count++;
    }
    return count;
}

int main()
{
    int n;
    scanf("%d", &n);
    int bar_size = next_power_of_two(n);
    printf("%d %d\n", bar_size, breaks_needed(bar_size, n));
    return 0;
}