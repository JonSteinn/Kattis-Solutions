#include <stdio.h>

char buffer[10];

void output(int n)
{
    fprintf(stdout, "%d\n", n);
    fflush(stdout);
}

int guess(int lo, int hi)
{
    int mid = lo + (hi-lo)/2;
    output(mid);
    scanf("%s", buffer);
    if (buffer[0] == 'c') return 0;
    return buffer[0] == 'l' ? guess(lo, mid-1) : guess(mid+1, hi);
}

int main()
{
    while (guess(1, 1000));
    return 0;
}