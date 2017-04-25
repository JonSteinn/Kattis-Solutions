#include <cstdio>
#include <algorithm>

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", arr + i);
    std::sort(arr, arr + n);
    int index = 0;
    while (index < n)
    {
        int start = arr[index];
        while(index + 1 < n && arr[index] == arr[index + 1] - 1) index++;
        int end = arr[index];
        if (start == end) printf("%d%s", start, index == n - 1 ? "\n" : " ");
        else if (start == end - 1) printf("%d %d%s", start, end, index == n - 1 ? "\n" : " ");
        else printf("%d-%d%s", start, end, index == n - 1 ? "\n" : " ");
        index++;
    }
    return 0;
}