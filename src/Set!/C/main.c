#include <stdio.h>

#define COUNT 12

int check(const char* s1, const char* s2, const char* s3)
{
    for (int x = 0; x < 4; x++)
    {
        if (!(s1[x] == s2[x] && s2[x] == s3[x]) && !(s1[x] != s2[x] && s1[x] != s3[x] && s2[x] != s3[x])) return 0;
    }
    return 1;
}

int main()
{
    char sets[COUNT][5];
    for (int i = 0; i < COUNT; i++) scanf("%s", sets[i]);
    int found = 0;
    for (int i = 0; i < COUNT; i++)
    {
        for (int j = i + 1; j < COUNT; j++)
        {
            for (int k = j + 1; k < COUNT; k++)
            {
                if (check(sets[i], sets[j], sets[k]))
                {
                    printf("%d %d %d\n", i + 1, j + 1, k + 1);
                    found = 1;
                }
            }
        }
    }
    if (!found) printf("no sets\n");
    return 0;
}