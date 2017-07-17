#include <stdio.h>
#include <stdlib.h>

typedef struct enumerate pair;
struct enumerate
{
    int index;
    int value;
};

int comparator(const void* a, const void* b)
{
    return ((pair*)b)->value - ((pair*)a)->value;
}

int read(int n, pair* exams)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &exams[i].value);
        exams[i].index = i + 1;
        sum += exams[i].value;
    }
    qsort(exams, (size_t)n, sizeof(pair), comparator);
    return sum;
}

int main()
{
    int n;
    scanf("%d",&n);
    pair exams[n];
    int total_exams = read(n, exams);
    if (total_exams < exams[0].value << 1) printf("impossible\n");
    else
    {
        printf("%d", exams[0].index);
        for (int i = 1; i < n; i++) printf(" %d", exams[i].index);
        putchar('\n');
    }
    return 0;
}