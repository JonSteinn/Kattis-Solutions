#include "string.h"
#include "stdio.h"

#define SIMON_SAYS "Simon says "
#define SIMON_LENGTH 11
#define MAX_BUFFER 101

int main()
{
    int n;
    scanf("%d", &n);
    while (n-- > 0)
    {
        char buffer[MAX_BUFFER];
        scanf(" %[^\n]", buffer);
        if (!strncmp(buffer, SIMON_SAYS, SIMON_LENGTH)) printf("%s\n", buffer + SIMON_LENGTH);
    }
}