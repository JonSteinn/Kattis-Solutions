#include <stdio.h>

int is_lower(char c)
{
    return c < 123 && c > 96;
}
int is_upper(char c)
{
    return c < 91 && c > 64;
}
int is_underscore(char c)
{
    return c == 95;
}
int main()
{
    int total = 0, lower = 0, upper = 0, whitespace = 0, symbol = 0;
    char buffer[100001];
    scanf("%s", buffer);
    int i;
    for (i = 0; i < 100001; i++)
    {
        if (buffer[i] == '\0') break;
        if (is_lower(buffer[i])) lower++;
        else if (is_upper(buffer[i])) upper++;
        else if (is_underscore(buffer[i])) whitespace++;
        else symbol++;
        total++;
    }

    printf("%.10f\n%.10f\n%.10f\n%.10f\n",
           (double)whitespace/total,(double)lower/total,(double)upper/total,(double)symbol/total);

    return 0;
}