#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 1000000
#define P_POS 'P'
#define N_POS 'N'
#define UNKNOWN 0

int comparator(const void* a, const void* b)
{
    return *((int*)a) - *((int*)b);
}

int n_pos(int n, int s, int* arr, char* pos)
{
    for (int i = 0; i <= n; i++)
    {
        if (pos[i] == UNKNOWN) pos[i] = P_POS;
        if (pos[i] == P_POS)
        {
            if (i < MAX_LEN - arr[s-1])
            {
                for (int j = 0; j < s; j++)
                {
                    pos[i + arr[j]] = N_POS;
                }
            }
            else
            {
                for (int j = 0; j < s; j++)
                {
                    if (i + arr[j] <= MAX_LEN) pos[i + arr[j]] = N_POS;
                }
            }
        }
    }
    return pos[n] == N_POS;
}

int main()
{
    char pos[MAX_LEN + 1];
    pos[0] = P_POS;
    int n, s;
    while(scanf("%d %d",&n,&s) == 2)
    {
        int arr[s];
        for (int i = 0; i < s; i++) scanf("%d", arr + i);
        qsort(arr, (size_t)s, sizeof(int), comparator);
        memset(pos + 1, 0, MAX_LEN * sizeof(char));
        printf(n_pos(n,s,arr, pos) ? "Stan wins\n" : "Ollie wins\n");
    }
    return 0;
}