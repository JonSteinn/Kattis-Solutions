#include <stdio.h>

#define MAX(a,b) ((a) < (b) ? (b) : (a))
#define MIN(a,b) ((a) > (b) ? (b) : (a))

struct in
{
    int guess;
    int status;
};

void input(struct in* x)
{
    char b1[10], b2[10];
    scanf("%d %s %s", &x->guess, b1, b2);
    if (b1[0] == 'r') x->status = 0;
    else if (b2[0] == 'h') x->status = 1;
    else x->status = -1;
}

int main()
{
    while(1)
    {
        int guess;
        scanf("%d",&guess);
        if (!guess) break;

        int high = 1000, low = -1;

        char buffer1[10], buffer2[10];
        scanf("%s %s", buffer1, buffer2);

        if (buffer1[0] != 'r')
        {
            if (buffer2[0] == 'h') high = MIN(high, guess);
            else low = MAX(low, guess);

            while(1)
            {
                struct in inp;
                input(&inp);

                if (inp.status)
                {
                    if (inp.status > 0) high = MIN(high, inp.guess);
                    else low = MAX(low, inp.guess);
                }
                else
                {
                    if (inp.guess < high && inp.guess > low && high > low)
                    {
                        printf("Stan may be honest\n");
                    }
                    else
                    {
                        printf("Stan is dishonest\n");
                    }
                    break;
                }

            }
        }
        else
        {
            printf("Stan may be honest\n");
        }
    }

    return 0;
}