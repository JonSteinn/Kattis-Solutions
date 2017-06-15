#include <stdio.h>

int main()
{
    int r, c;
    scanf("%d %d", &r, &c);
    char seats[r][c + 1];
    for (int i = 0; i < r; i++) scanf("%s",seats[i]);
    int n_index[] = {-1,0,1};
    long long total = 0;
    int most = 0;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (seats[i][j] == '.')
            {
                if (most < 9)
                {
                    int count = 0;
                    for (int x = 0; x < 3; x++)
                    {
                        for (int y = 0; y < 3; y++)
                        {
                            if (!n_index[x] && !n_index[y]) continue;
                            int n_i = i + n_index[x];
                            if (n_i < 0 || n_i >= r) continue;
                            int n_j = j + n_index[y];
                            if (n_j < 0 || n_j >= c) continue;
                            if (seats[n_i][n_j] == 'o') count++;
                        }
                    }
                    if (count > most) most = count;
                }
            }
            else
            {
                int count = 0;
                for (int x = 0; x < 3; x++)
                {
                    for (int y = 0; y < 3; y++)
                    {
                        if (!n_index[x] && !n_index[y]) continue;
                        int n_i = i + n_index[x];
                        if (n_i < 0 || n_i >= r) continue;
                        int n_j = j + n_index[y];
                        if (n_j < 0 || n_j >= c) continue;
                        if (seats[n_i][n_j] == 'o') count++;
                    }
                }
                total += count;
            }
        }
    }
    printf("%lld\n", (total >> 1) + most);
    return 0;
}