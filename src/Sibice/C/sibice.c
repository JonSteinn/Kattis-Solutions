#include <stdio.h>

int main()
{
    int n, w, h;
    scanf("%d %d %d", &n, &w, &h);
    double max_len_squared = w*w + h*h;
    while(n--)
    {
        int match;
        scanf("%d", &match);
        printf(match * match <= max_len_squared ? "DA\n" : "NE\n");
    }
    return 0;
}