#include <stdio.h>
#include <string.h>
int main()
{
    char buffer[100001];
    scanf("%s",buffer);
    size_t len = strlen(buffer);
    int counters[] = {0, 0};
    for (size_t i = 0; i < len; i++) counters[buffer[i] == 'W']++;
    printf("%d\n", counters[0] == counters[1]);
    return 0;
}