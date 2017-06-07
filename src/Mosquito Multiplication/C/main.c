#include <stdio.h>

int main()
{
    int M,P,L,E,R,S,N;
    while (scanf("%d %d %d %d %d %d %d",&M,&P,&L,&E,&R,&S,&N) == 7)
    {
        while(N--)
        {
            int tmp_p = P;
            P = L / R;
            L = E * M;
            M = tmp_p / S;
        }
        printf("%d\n",M);
    }
    return 0;
}