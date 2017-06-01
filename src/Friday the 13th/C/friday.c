#include <stdio.h>

void experiment()
{
    int d, m;
    scanf("%d %d", &d, &m);
    int arr[m];
    for (int i = 0; i < m; i++) scanf("%d", arr + i);
    int current_day = 0, current_month = 0, count = 0;
    while (d)
    {
        if (arr[current_month] > 12 && ((current_day + 12) % 7 == 5)) count++;
        d -= arr[current_month];
        current_day = (current_day + arr[current_month]) % 7;
        current_month++;
    }
    printf("%d\n", count);
}

int main()
{
    int n;
    scanf("%d", &n);
    while(n--) experiment();
    return 0;
}