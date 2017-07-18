#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        fprintf(stdout, "5 1 5 6\n");
        fflush(stdout);
        while(1)
        {
            char command[5];
            scanf("%s", command);
            if (command[0] != 'M') break;
            int r1, c1, r2, c2;
            scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
            if (r2 == 5) r2--;
            fprintf(stdout, "%d %d %d %d\n", 5 - r2, 7 - c2, 5 - r1, 7 - c1);
            fflush(stdout);
        }

    }
    return 0;
}