#include <stdio.h>
#include <string.h>

#define INF 2147483647

int max(int a, int b)
{
    return a < b ? b : a;
}

int min (int a, int b)
{
    return a < b ? a : b;
}

// m = mailboxes
// a = highest known number that does not blow up mailbox
// b = highest known number that will not blow up mailbox
int crackers(int m, int a, int b, int* memory)
{
    int index = b * 1111 + a * 11 + m;
    if (memory[index] < 0)
    {
        if (m == 1) return (b * (b + 1) - a * (a + 1)) >> 1;
        if (b <= a) return 0;
        int least = INF;
        for (int i = a + 1; i < b + 1; i++)
        {
            least = min(i + max(crackers(m-1, a, i - 1, memory), crackers(m, i, b, memory)), least);
        }
        memory[index] = least;
    }
    return memory[index];
}

int main()
{
    int memory[112211];
    memset(memory, -1, sizeof(int) * 112211);
    int n;
    scanf("%d",&n);
    while(n--)
    {
        int m, b;
        scanf("%d %d",&m,&b);
        printf("%d\n", crackers(m, 0, b, memory));
    }
    return 0;
}