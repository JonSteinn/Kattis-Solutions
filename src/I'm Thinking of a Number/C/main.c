#include <stdio.h>

#define PINF 50001
#define NINF 0

int start(int a, int max_div)
{
    return max_div < 0 ? a + 1 : a < max_div ? max_div : (a + 1) + (max_div - (a + 1) % max_div);
}

void generate(int a, int b, int* divs, int div_count, int max_div)
{
    int at_least_one = 0;
    for (int i = start(a, max_div); i < b; i += max_div)
    {
        int divisible_by_all = 1;
        for (int j = 0; j < div_count; j++)
        {
            if (i % divs[j])
            {
                divisible_by_all = 0;
                break;
            }
        }
        if (divisible_by_all)
        {
            at_least_one = 1;
            printf("%d ", i);
        }
    }
    printf(at_least_one ? "\n" : "none\n");
}

void swap(int i, int j, int* arr)
{
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void test_case(int n)
{
    int value, upper_bound = PINF, lower_bound = NINF, max_div = -1, max_div_index = -1, curr_index = 0;
    int divs[n];
    char cmd[10], dmp[5];

    for (int i = 0; i < n; i++)
    {
        scanf("%s %s %d", cmd, dmp, &value);
        if (cmd[0] == 'l')
        {
            if (value < upper_bound) upper_bound = value;
        }
        else if (cmd[0] == 'g')
        {
            if (value > lower_bound) lower_bound = value;
        }
        else
        {
            if (max_div < value)
            {
                max_div = value;
                max_div_index = curr_index;
            }
            divs[curr_index++] = value;
        }
    }

    if (upper_bound == PINF) printf("infinite\n");
    else if (upper_bound <= lower_bound + 1) printf("none\n");
    else if (curr_index == 0)
    {
        for (int i = lower_bound + 1; i < upper_bound; i++) printf("%d ", i);
        printf("\n");
    }
    else if (curr_index == 1)
    {
        generate(lower_bound, upper_bound, NULL, 0, max_div);
    }
    else
    {
        curr_index--;
        if (max_div_index != curr_index) swap(max_div_index, curr_index, divs);
        generate(lower_bound, upper_bound, divs, curr_index, max_div);
    }
}

int main()
{
    while(1)
    {
        int n;
        scanf("%d", &n);
        if (!n) break;
        test_case(n);
    }
    return 0;
}