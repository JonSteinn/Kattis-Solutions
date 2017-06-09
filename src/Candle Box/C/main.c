#include <stdio.h>

int find_age(int candles, int offset)
{
    candles += offset;
    candles <<= 1;
    int x = 0;
    while (x * x + x - candles < 0) x++;
    return x * x + x - candles == 0 ? x : -1;
}

int main()
{
    int d,r,t;
    scanf("%d %d %d",&d,&r,&t);
    int candle_transfers = 0;
    while(1)
    {
        int r_age = find_age(r--, 6);
        int t_age = find_age(t++, 3);
        if (r_age - t_age == d) break;
        candle_transfers++;
    }
    printf("%d\n", candle_transfers);
    return 0;
}