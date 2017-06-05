#include <iostream>
#include <unordered_map>
#include <sstream>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::unordered_map<std::string, std::string> dictionary;
    std::string line;
    bool add = true;
    while (std::getline(std::cin, line))
    {
        std::istringstream ss(line);
        std::string first;
        ss >> first;
        if (add)
        {
            if (ss.eof())
            {
                add = false;
                continue;
            }
            else
            {
                std::string second;
                ss >> second;
                dictionary[second] = first;
            }
        }
        else
        {
            if (dictionary.find(first) == dictionary.end()) std::cout << "eh\n";
            else std::cout << dictionary[first] << "\n";
        }
    }
    return 0;
}