#include <stdio.h>

int radii_squared[] = {400,1600,3600,6400,10000,14400,19600,25600,32400,40000};

int score(int x, int y)
{
    int radius_squared = x * x + y * y;
    int p = -1;
    for (int i = 0; i < 10; i++)
    {
        if (radius_squared <= radii_squared[i])
        {
            p = 10 - i;
            break;
        }
    }
    return p < 0 ? 0 : p;
}

int total_score()
{
    int darts, _score = 0;
    scanf("%d",&darts);
    while(darts--)
    {
        int x, y;
        scanf("%d %d",&x,&y);
        _score += score(x,y);
    }
    return _score;
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) printf("%d\n", total_score());
    return 0;
}