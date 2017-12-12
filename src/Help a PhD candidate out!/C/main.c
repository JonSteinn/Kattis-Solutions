#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n = 0;
    scanf("%d",&n);
    char buffer[10];
    while(n--)
    {
        scanf("%s", buffer);
        if (buffer[0] == 'P')
        {
            printf("skipped\n");
            continue;
        }
        int index = 0;
        while (*(buffer + index) != '+') index++;
        buffer[index] = '\0';
        printf("%d\n", atoi(buffer) + atoi(buffer + index + 1));
    }
    return 0;
}