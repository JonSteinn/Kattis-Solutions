#include <iostream>
#include <unordered_map>
#include <vector>
#include <set>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::unordered_map<std::string,std::vector<std::string>> _map;

    std::string in;
    while(std::cin >> in)
    {
        std::vector<std::string> vec;
        for (auto it = _map.begin(); it != _map.end(); ++it)
        {
            if (it->first != in) it->second.push_back(in);
            else vec.push_back(it->first);
        }
        _map[in] = vec;
    }

    std::set<std::string> _set;
    for (auto it = _map.begin(); it != _map.end(); ++it)
    {
        std::vector<std::string> vec = it->second;
        for (auto it2 = vec.begin(); it2 != vec.end(); ++it2)
        {
            _set.insert(it->first + *it2);
            _set.insert(*it2 + it->first);
        }
    }

    for (auto it = _set.begin(); it != _set.end(); ++it)
    {
        std::cout << *it << "\n";
    }

    return 0;
}