#include <stdio.h>

int main()
{
    int in, out = 0;
    scanf("%d", &in);
    while (in)
    {
        out = (out << 1) | (in & 1);
        in >>= 1;
    }
    printf("%d\n", out);
    return 0;
}