#include <stdio.h>
#include <stdlib.h>

int comparator(const void* a, const void *b)
{
    return *((int*)b) - *((int*)a);
}

int cars_needed(int* space, int people)
{
    int counter = 0;
    int index = 0;
    while (people > 0)
    {
        people -= space[index++];
        counter++;
    }
    return counter;
}

void test_case(int tc)
{
    printf("Case #%d:", tc);

    int n,t,e;
    scanf("%d %d %d",&n,&t,&e);
    t--;
    int seats[n][e];

    size_t* employees = (size_t*)calloc((size_t)(n<<1), sizeof(size_t));
    size_t* sums = employees + n;

    for (int i = 0; i < e; i++)
    {
        int h,p;
        scanf("%d %d",&h,&p);
        h--;

        seats[h][employees[h]] = p;
        employees[h]++;
        sums[h] += p;
    }

    int valid = 1;

    for (int i = 0; i < n; i++)
    {
        if (employees[i])
        {
            if (i != t && sums[i] < employees[i])
            {
                valid = 0;
                break;
            }
            qsort(seats[i], employees[i], sizeof(int), comparator);
        }
    }

    if (valid)
    {
        for (int i = 0; i < n; i++)
        {
            if (i == t || employees[i] == 0) printf(" 0");
            else printf(" %d", cars_needed(seats[i], (int)employees[i]));
        }
        printf("\n");
    }
    else
    {
        printf(" IMPOSSIBLE\n");
    }

}

int main()
{
    int n;
    scanf("%d",&n);
    for (int i = 1; i <= n; i++) test_case(i);
    return 0;
}