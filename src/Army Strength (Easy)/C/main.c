#include <stdio.h>
#include <stdlib.h>

int comparator(const void* a, const void* b)
{
    return *((short*)a) - *((short*)b);
}

int fight(short* arr1, int n1, short* arr2, int n2)
{
    qsort(arr1, (size_t)n1, sizeof(short), comparator);
    qsort(arr2, (size_t)n2, sizeof(short), comparator);
    int curr_g = 0, curr_m = 0;
    while(curr_g < n1 && curr_m < n2)
    {
        if (arr1[curr_g] < arr2[curr_m]) curr_g++;
        else curr_m++;
    }
    return n1 - curr_g;
}

void test_case()
{
    int g, m;
    scanf("%d %d",&g,&m);
    short army_g[g];
    short army_m[m];
    for (int i = 0; i < g; i++) scanf("%hi",army_g+i);
    for (int i = 0; i < m; i++) scanf("%hi",army_m+i);
    printf(fight(army_g, g, army_m, m) ? "Godzilla\n" : "MechaGodzilla\n");
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}