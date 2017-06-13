#include <stdio.h>

int main()
{
    int a, b, d;
    while (scanf("%d %d %d",&a,&b,&d) == 3)
    {
        int len = d + 3;
        char buffer[len];
        int i = 0;
        buffer[len - 1] = '\0'; buffer[i++] = '0'; buffer[i++] = '.';
        while (i < len - 1)
        {
            if (a < b)
            {
                a *= 10;
                int n = a / b;
                buffer[i++] = (char)('0' + n);
                a -= n * b;
                if (a == 0)
                {
                    while (i < len - 1)
                    {
                        buffer[i++] = '0';
                    }
                }
            }
            else
            {
                buffer[i++] = (char)('0' + 1);
                a -= b;
            }
        }
        printf("%s\n",buffer);
    }
    return 0;
}
