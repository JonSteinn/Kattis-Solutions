#include <stdio.h>

#define P1 "Player 1 wins.\n"
#define P2 "Player 2 wins.\n"
#define D "Tie.\n"
#define MAX_SCORE 1000
#define TIE_SCORE 100

int score(int s, int r)
{
    return s + r == 3 ? MAX_SCORE : (s == r ? TIE_SCORE : (s < r ? r * 10 + s : s * 10 + r));
}

void game(int s0, int r0, int s1, int r1)
{
    int p1 = score(s0, r0), p2 = score(s1, r1);
    printf(p1 > p2 ? P1 : (p1 < p2 ? P2 : (p1 == TIE_SCORE ? (s0 > s1 ? P1 : (s0 < s1 ? P2 : D)) : D)));
}

int main()
{
    while (1)
    {
        int s0, r0, s1, r1;
        scanf("%d %d %d %d", &s0, &r0, &s1, &r1);
        if (!s0 && !r0 && !s1 && !r1) break;
        game(s0, r0, s1, r1);
    }
    return 0;
}