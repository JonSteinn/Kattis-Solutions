#include <stdio.h>
#include <stdlib.h>

#define P1 1
#define P2 2
#define D 0

int result(char p1, char p2)
{
    return p1 == p2 ? D : (p1 == 'r' ? (p2 == 's' ? P1 : P2) : (p1 == 'p' ? (p2 == 'r' ? P1 : P2) : (p2 == 'p' ? P1 : P2)));
}

int tournament(int players, int games)
{
    int* won = (int*)calloc((size_t)players << 1, sizeof(int));
    int* lost = won + players;
    while(games--)
    {
        int p1, p2;
        char buffer1[9], buffer2[9];
        scanf("%d %s %d %s",&p1,buffer1,&p2,buffer2);
        p1--; p2--;
        int r = result(buffer1[0],buffer2[0]);
        if (r == 1)
        {
            won[p1]++;
            lost[p2]++;
        }
        else if (r == 2)
        {
            won[p2]++;
            lost[p1]++;
        }
    }
    for (int i = 0; i < players; i++)
    {
        if (won[i]+lost[i] == 0) printf("-\n");
        else printf("%.3lf\n", ((double)won[i]) / (won[i]+lost[i]));
    }
    free(won);
}

int main()
{
    int first = 1;
    while(1)
    {
        int n;
        scanf("%d",&n);
        if (!n) break;
        if (first) first = 0;
        else printf("\n");
        int k;
        scanf("%d",&k);
        tournament(n,k * n * (n-1) >> 1);
    }
    return 0;
}