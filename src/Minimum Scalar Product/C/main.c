#include <stdio.h>
#include <stdlib.h>

int comparator(const void *n1, const void *n2)
{
    int l = *((int*)n1), r = *((int*)n2);
    return l > r ? 1 : l < r ? -1 : 0;
}

int rev_comparator(const void *n1, const void *n2)
{
    int l = *((int*)n1), r = *((int*)n2);
    return l > r ? -1 : l < r ? 1 : 0;
}

void test_case(int tc)
{
    int n;
    scanf("%d",&n);
    int v1[n], v2[n];
    for (int i = 0; i < n; i++) scanf("%d",v1+i);
    for (int i = 0; i < n; i++) scanf("%d",v2+i);
    qsort(v1, (size_t)n, sizeof(int), comparator);
    qsort(v2, (size_t)n, sizeof(int), rev_comparator);
    long long sum = 0;
    for (int i = 0; i < n; i++)
    {
        long long next = v1[i];
        next *= v2[i];
        sum += next;
    }
    printf("Case #%d: %lld\n",tc,sum);
}

int main()
{
    int tc;
    scanf("%d",&tc);
    for (int i = 1; i <= tc; i++) test_case(i);
    return 0;
}