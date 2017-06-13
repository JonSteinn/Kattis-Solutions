#include <unordered_map>
#include <iostream>

void fill(std::unordered_map<std::string,int>& m, int n)
{
    while(n--)
    {
        std::string s;
        std::cin >> s;
        m[s] = m.find(s) == m.end() ? 1 : m[s] + 1;
    }
}

int min(int a, int b)
{
    return a < b ? a : b;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int n;
    std::cin >> n;

    std::unordered_map<std::string,int> dom, kat;
    fill(dom, n);
    fill(kat, n);

    int count = 0;
    for (std::unordered_map<std::string,int>::iterator it = dom.begin(); it != dom.end(); ++it)
    {
        if (kat.find(it->first) != kat.end())
        {
            count += min(it->second, kat.find(it->first)->second);
        }
    }

    std::cout << count << std::endl;
    return 0;
}