#include <stdio.h>
#include <string.h>

int main()
{
    char buffer1[1001], buffer2[1001];
    scanf("%s", buffer1);
    scanf("%s", buffer2);
    printf(strlen(buffer1) < strlen(buffer2) ? "no\n" : "go\n");
}