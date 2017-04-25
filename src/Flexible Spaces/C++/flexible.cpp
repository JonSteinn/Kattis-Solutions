#include <cstdio>
#include <set>

int main()
{
    int w, p;
    scanf("%d %d", &w, &p);
    int arr[p + 2];
    for (int i = 1; i <= p; i++) scanf("%d", arr + i);
    arr[0] = 0; arr[p + 1] = w;
    std::set<int> _set;
    for (int i = 0; i < p + 2; i++) for (int j = 0; j < i; j++) _set.insert(arr[i] - arr[j]);
    int index = 0;
    for (std::set<int>::iterator it = _set.begin(); it != _set.end(); ++it) printf(index++ == _set.size() - 1 ? "%d\n" : "%d ", *it);
    return 0;
}