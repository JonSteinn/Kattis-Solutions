#include <stdio.h>

int check(char* str)
{
    int s = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (s & (1 << (str[i] - 'a')))
        {
            return 0;
        }
        else
        {
            s |= (1 << (str[i] - 'a'));
        }
    }
    return 1;
}

int main() 
{
    char buffer[51];
    scanf("%s", buffer);
    printf("%d\n", check(buffer));
    return 0;
}