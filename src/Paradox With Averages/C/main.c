#include <stdio.h>

void test_case()
{
    int cs, e;
    scanf("%d %d", &cs, &e);
    long long cs_total = 0L, e_total = 0L;
    int cs_students[cs], e_students[e];
    for (int i = 0; i < cs; i++)
    {
        scanf("%d", cs_students + i);
        cs_total += cs_students[i];
    }
    for (int i = 0; i < e; i++)
    {
        scanf("%d", e_students + i);
        e_total += e_students[i];
    }

    double cs_av = cs_total / (double)cs;
    double e_av = e_total / (double)e;

    int counter = 0;
    for (int i = 0; i < cs; i++)
    {
        if (cs_students[i] < cs_av && cs_students[i] > e_av) counter++;
    }
    printf("%d\n",counter);
}

int main()
{
    int n;
    scanf("%d",&n);
    while(n--) test_case();
    return 0;
}