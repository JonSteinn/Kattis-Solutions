#include <stdio.h>
#include <string.h>

#define SIMON "simon says "
#define SIMON_LEN 11

int main()
{
    int n;
    scanf("%d\n",&n);
    char buffer[1001];
    while(n-->0)
    {
        fgets(buffer, 1001, stdin);
        size_t len = strlen(buffer);
        if (len <= SIMON_LEN || strncmp(buffer, SIMON, SIMON_LEN)) printf("\n");
        else printf("%s\n", buffer+SIMON_LEN);
    }
    return 0;
}