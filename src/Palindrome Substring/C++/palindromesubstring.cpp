#include <iostream>
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <queue>

bool is_palindrome(const std::string &str, size_t lo, size_t hi)
{
    while (lo < hi + 1)
    {
        if (str[lo] != str[hi]) return false;
        lo++;
        hi--;
    }
    return true;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    std::string word;
    while (std::cin >> word)
    {
        std::unordered_map<char, std::vector<size_t>> char_occurrences;
        std::unordered_set<std::string> palindromes;
        std::priority_queue<std::string, std::vector<std::string>, std::greater<std::string>> ordered_palindromes;
        for (size_t i = 0; i < word.length(); i++) char_occurrences[word[i]].push_back(i);

        for (size_t i = 0; i < word.length(); i++)
        {
            std::vector<size_t> vec = char_occurrences[word[i]];
            for (std::vector<size_t>::iterator it = vec.begin(); it != vec.end(); ++it)
            {
                if (*it <= i) continue;
                if (is_palindrome(word, i, *it))
                {
                    std::string sub_string = word.substr(i, *it - i + 1);
                    if (palindromes.find(sub_string) == palindromes.end())
                    {
                        palindromes.insert(sub_string);
                        ordered_palindromes.push(sub_string);
                    }
                    printf("\n");
                }
            }
        }

        while (!ordered_palindromes.empty())
        {
            std::cout << ordered_palindromes.top() << "\n";
            ordered_palindromes.pop();
        }
    }
    return 0;
}