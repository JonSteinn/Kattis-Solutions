#include <stdio.h>

#define S1 "single"
#define S2 "double"
#define S3 "triple"
#define AMOUNT(x) ((x) == 0 ? S1 : (x) == 1 ? S2 : S3)

int scores[] =
{
    1,2,3,
    2,4,6,
    3,6,9,
    4,8,12,
    5,10,15,
    6,12,18,
    7,14,21,
    8,16,24,
    9,18,27,
    10,20,30,
    11,22,33,
    12,24,36,
    13,26,39,
    14,28,42,
    15,30,45,
    16,32,48,
    17,34,51,
    18,36,54,
    19,38,57,
    20,40,60
};

// Just gonna brute force this, 60^3 isn't large...
void hits(int score)
{
    for (int i = 0; i < 60; i++)
    {
        if (scores[i] == score)
        {
            printf("%s %d\n", AMOUNT(i % 3), i / 3 + 1);
            return;
        }
        for (int j = 0; j < 60; j++)
        {
            if (scores[i] + scores[j] == score)
            {
                printf("%s %d\n", AMOUNT(i % 3), i / 3 + 1);
                printf("%s %d\n", AMOUNT(j % 3), j / 3 + 1);
                return;
            }
            for (int k = 0; k < 60; k++)
            {
                if (scores[i] + scores[j] + scores[k] == score)
                {
                    printf("%s %d\n", AMOUNT(i % 3), i / 3 + 1);
                    printf("%s %d\n", AMOUNT(j % 3), j / 3 + 1);
                    printf("%s %d\n", AMOUNT(k % 3), k / 3 + 1);
                    return;
                }
            }
        }
    }
    printf("impossible\n");
}

int main()
{
    int n;
    scanf("%d",&n);
    hits(n);
    return 0;
}