#include <stdio.h>

#define ROCK 82
#define PAPER 80
#define SCISSORS 83

void test_case()
{
    int r, c, d;
    scanf("%d %d %d",&r,&c,&d);
    char mats[2][r][c + 1];
    for (int i = 0; i < r; i++)
    {
        scanf("%s", mats[0][i]);
        mats[1][i][c] = '\0';
    }
    for (int i = 0; i < d; i++)
    {
        int prev_mat = i&1;
        int next_mat = !prev_mat;

        for (int _r = 0; _r < r; _r++)
        {
            for (int _c = 0; _c < c; _c++)
            {
                char l = (char)(mats[prev_mat][_r][_c] == ROCK ? PAPER : mats[prev_mat][_r][_c] == SCISSORS ? ROCK : SCISSORS);
                mats[next_mat][_r][_c] =
                        (_r > 0 && mats[prev_mat][_r - 1][_c] == l || _r < r - 1 && mats[prev_mat][_r + 1][_c] == l ||
                         _c > 0 && mats[prev_mat][_r][_c - 1] == l || _c < c - 1 && mats[prev_mat][_r][_c + 1] == l)
                        ? l : mats[prev_mat][_r][_c];
            }
        }
    }
    int end_mat = d&1;
    for (int _r = 0; _r < r; _r++) printf("%s\n", mats[end_mat][_r]);
}

int main()
{
    int n;
    scanf("%d",&n);
    int first = 1;
    while(n--)
    {
        if (first) first = 0;
        else printf("\n");
        test_case();
    }
    return 0;
}