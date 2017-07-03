#include <stdio.h>

int main()
{
    int r, c;
    scanf("%d %d",&r,&c);
    char lot[r][c + 1];
    for (int i = 0; i < r; i++) scanf("%s",lot[i]);
    int counters[] = {0,0,0,0,0};
    for (int i = 0; i < r - 1; i++)
    {
        for (int j = 0; j < c - 1; j++)
        {
            if (lot[i][j] != '#' && lot[i][j+1] != '#' && lot[i+1][j] != '#' && lot[i+1][j+1] != '#')
            {
                counters[(lot[i][j] == 'X' ? 1 : 0) + (lot[i][j+1] == 'X' ? 1 : 0) + (lot[i+1][j] == 'X' ? 1 : 0) + (lot[i+1][j+1] == 'X' ? 1 : 0)]++;
            }
        }
    }
    for (int i = 0; i < 5; i++) printf("%d\n", counters[i]);
    return 0;
}