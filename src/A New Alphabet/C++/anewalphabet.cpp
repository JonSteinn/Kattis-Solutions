#include <cstdio>
#include <string>
#include <unordered_map>
#include <cstring>

int main()
{
    std::unordered_map<char, std::string> alpha_map{
            {'A', "@"},
            {'B', "8"},
            {'C', "("},
            {'D', "|)"},
            {'E', "3"},
            {'F', "#"},
            {'G', "6"},
            {'H', "[-]"},
            {'I', "|"},
            {'J', "_|"},
            {'K', "|<"},
            {'L', "1"},
            {'M', "[]\\/[]"},
            {'N', "[]\\[]"},
            {'O', "0"},
            {'P', "|D"},
            {'Q', "(,)"},
            {'R', "|Z"},
            {'S', "$"},
            {'T', "']['"},
            {'U', "|_|"},
            {'V', "\\/"},
            {'W', "\\/\\/"},
            {'X', "}{"},
            {'Y', "`/"},
            {'Z', "2"}
    };
    char c;
    while (scanf("%c", &c) > 0)
    {
        if ('a' <= c && c <= 'z') printf("%s", alpha_map[c - 32].c_str());
        else if ('A' <= c && c <= 'Z') printf("%s", alpha_map[c].c_str());
        else printf("%c", c);
    }
    return 0;
}