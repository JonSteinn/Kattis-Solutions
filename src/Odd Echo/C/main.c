#include <stdio.h>

int main() 
{
    int n;
    char buffer[101];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s", buffer);
        if (!(i & 1))
        {
            printf("%s\n", buffer);
        }
    }
    return 0;
}