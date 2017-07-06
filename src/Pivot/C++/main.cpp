#include <stdio.h>
#include <set>

int main()
{
    int n;
    scanf("%d",&n);
    std::set<int> pivots;
    int largest_so_far = -2147483648;
    for (int i = 0; i < n; i++)
    {
        int next;
        scanf("%d", &next);
        pivots.erase(pivots.upper_bound(next), pivots.end());
        if (next > largest_so_far)
        {
            largest_so_far = next;
            pivots.insert(next);
        }
    }
    printf("%llu\n", pivots.size());
    return 0;
}
