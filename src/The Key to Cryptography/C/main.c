#include <stdio.h>
#include <string.h>

int main()
{
    char buffer1[1503];
    char* buffer2 = buffer1 + 501;
    char* buffer3 = buffer1 + 1002;

    scanf("%s", buffer1);
    scanf("%s", buffer2);

    size_t len1 = strlen(buffer1);
    size_t len2 = strlen(buffer2);
    size_t min_len = len1 < len2 ? len1 : len2;
    
    int index_in = 0, index_out = 0;

    for (size_t i = 0; i < min_len; i++)
    {
        buffer3[index_in++] = (char)(((buffer1[i] - buffer2[i] + 26) % 26) + 65);
    }

    for (size_t i = len2; i < len1; i++)
    {
        buffer3[index_in++] = (char)(((buffer1[i] - buffer3[index_out++] + 26) % 26) + 65);
    }

    buffer3[index_in] = '\0';
    printf("%s\n", buffer3);

    return 0;
}
