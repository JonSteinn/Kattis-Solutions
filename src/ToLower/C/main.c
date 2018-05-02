#include <stdio.h>
#include <string.h>

int main()
{
    int p = 0, t = 0, c = 0;
    char str[50001];
    scanf("%d %d", &p, &t);
    while(p--)
    {
        int valid = 1;
        for (int i = 0; i < t; i++)
        {
            scanf("%s", str);
            if (!valid) continue;
            size_t len = strlen(str);
            for (int j = 1; j < len; j++)
            {
                if (str[j] <= 'Z' && str[j] >= 'A')
                {
                    valid = 0;
                    break;
                }
            }
        }
        if (valid) c++;
    }
    printf("%d\n", c);
    return 0;
}