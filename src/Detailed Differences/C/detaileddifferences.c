#include <stdio.h>

void test_case()
{
    char buffer1[501], buffer2[501];
    scanf("%s", buffer1);
    scanf("%s", buffer2);
    printf("%s\n%s\n", buffer1, buffer2);
    int index = -1;
    while (buffer1[++index] != 0) printf("%c", buffer1[index] == buffer2[index] ? '.' : '*');
    printf("\n");
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n-- > 0) test_case();
    return 0;
}