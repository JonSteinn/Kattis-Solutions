#include <stdio.h>
#include <string.h>

int main()
{
    int n;
    scanf("%d",&n);
    while(n--)
    {
        char buffer[7];
        scanf("%s",buffer);
        size_t index = strlen(buffer) - 1;
        while (index > 0 && buffer[index] == '0') index--;
        if (index == 0 && buffer[index] == '1') printf("0\n");
        else
        {
            buffer[index] = (char)(buffer[index] - 1);
            printf("%s\n", buffer);
        }

    }
    return 0;
}