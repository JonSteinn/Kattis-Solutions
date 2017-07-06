#include <stdio.h>
#include <string.h>

int main()
{
    char b[51];
    scanf("%s",b);
    size_t len = strlen(b);
    int ball = 1;
    for (int i = 0; i < len; i++)
    {
        ball = b[i] == 'A' ? (ball == 1 ? 2 : (ball == 2 ? 1 : 3)) :
               (b[i] == 'B' ? (ball == 2 ? 3 : (ball == 3 ? 2 : 1)) : (ball == 1 ? 3 : (ball == 3 ? 1 : 2)));
    }
    printf("%d\n",ball);
    return 0;
}