#include <stdio.h>
#include <string.h>

int matches(char n, char c)
{
    return (n == '2' && c <= 'c') ||
           (n == '3' && c <= 'f') ||
           (n == '4' && c <= 'i') ||
           (n == '5' && c <= 'l') ||
           (n == '6' && c <= 'o') ||
           (n == '7' && c <= 's') ||
           (n == '8' && c <= 'v') ||
           (n == '9' && c <= 'z');
}

int main()
{
    int n;
    scanf("%d",&n);
    char strings[n][1001];
    char number[1001];
    for (int i = 0; i < n; i++) scanf("%s",strings[i]);
    scanf("%s",number);
    size_t num_len = strlen(number);
    int counter = 0;
    for (int i = 0; i < n; i++)
    {
        size_t len = strlen(strings[i]);
        if (num_len != len) continue;

        for (int j = 0; j < len; j++)
        {
            if (!matches(number[j], strings[i][j])) break;
            if (j == len - 1) counter++;
        }
    }
    printf("%d\n",counter);
    return 0;
}