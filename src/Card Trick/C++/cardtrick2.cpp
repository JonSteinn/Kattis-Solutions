#include <cstdio>
#include <vector>
#include <list>

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        int k;
        scanf("%d", &k);
        std::vector<int> v;
        for (int i = 1; i <= k; i++) v.push_back(i);
        std::list<int> lst;
        int numberOfShifts = k;
        for (int i = k - 1; i >= 0; i--)
        {
            lst.push_front(v[i]);
            for (int i = 0; i < numberOfShifts; i++)
            {
                int tmp = lst.back();
                lst.pop_back();
                lst.push_front(tmp);
            }
            numberOfShifts--;
        }
        int ind = 0;
        for (std::list<int>::iterator it = lst.begin(); it != lst.end(); ++it)
        {
            printf(ind == lst.size() - 1 ? "%d\n" : "%d ", *it);
            ind++;
        }
    }
    return 0;
}