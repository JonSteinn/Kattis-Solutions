#include <stdio.h>
#include <unordered_set>
#include <unordered_map>

int sum(int* arr, int subset)
{
    int s = 0;
    int i = 0;
    while(subset)
    {
        if (subset&1) s += arr[i];
        i++;
        subset >>= 1;
    }
    return s;
}

void out(int* arr, int subset)
{
    bool first = true;
    int index = 0;

    while (subset)
    {
        if (subset&1)
        {
            if (first)
            {
                printf("%d", arr[index]);
                first = false;
            }
            else
            {
                printf(" %d", arr[index]);
            }
        }
        subset >>= 1;
        index++;
    }
    printf("\n");
}

void find(int upper, int* arr, const std::unordered_set<int>& singles, std::unordered_map<int,int>& ss_map)
{
    bool found = false;
    for (int i = 3; i < upper; i++)
    {
        if (i&(i-1))
        {
            int s = sum(arr, i);
            if (singles.find(s) != singles.end())
            {
                out(arr, i);
                printf("%d\n", s);
                found = true;
                break;
            }
            else if (ss_map.find(s) != ss_map.end())
            {
                out(arr, ss_map[s]);
                out(arr, i);
                found = true;
                break;
            }
            else
            {
                ss_map[s] = i;
            }
        }
    }
    if (!found) printf("Impossible\n");
}

void test_case(int tc)
{
    printf("Case #%d:\n", tc);
    scanf("%d",&tc); // dump
    int upper = (1 << 20) - 1;
    int arr[20];
    std::unordered_set<int> singles(41);
    std::unordered_map<int, int> ss_map(1 << 21);
    for (int i = 0; i < 20; i++)
    {
        scanf("%d", arr+i);
        singles.insert(arr[i]);
    }
    find(upper, arr, singles, ss_map);
}

int main()
{
    int n;
    scanf("%d\n",&n);
    for (int i = 1; i <= n; i++) test_case(i);
    return 0;
}