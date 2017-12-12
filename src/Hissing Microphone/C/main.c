#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[31];
    scanf("%s", buffer);
    printf(strstr(buffer, "ss") == NULL ? "no hiss\n" : "hiss\n");
    return 0;
}