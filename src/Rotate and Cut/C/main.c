#include <stdio.h>
#include <string.h>

void cuts(char* str, int lo, int hi, int n)
{
    int front = 1;
    int elements = hi - lo + 1;
    while(n--)
    {
        if (elements < 4) break;
        int quarter = elements >> 2;
        elements -= quarter;
        if (front) lo += quarter;
        else hi -= quarter;
        front = !front;
    }
    str[hi+1] = '\0';
    printf("%s\n", str + lo);
}

void test_case()
{
    int n;
    char buffer[2001];
    scanf("%d %s",&n,buffer);
    cuts(buffer, 0, (int)strlen(buffer) - 1, n);
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}