#include <stdio.h>
#include <string.h>
#include <unordered_set>
#include <unordered_map>

#define IS_SET(x,bit) ((x) & (1<<(bit)))
#define SET(x,bit) ((x) |= (1<<(bit)))
#define GET_INDEX(x) ((x) - 'a')

void find(std::unordered_map<char, std::unordered_set<char>> &map, char from, char goal, int &checked, bool &found)
{
    if (map.find(from) == map.end()) return;
    for (std::unordered_set<char>::iterator it = map[from].begin(); it != map[from].end(); ++it)
    {
        if (found) break;
        if (IS_SET(checked, GET_INDEX(*it))) continue;
        if (*it == goal) found = true;
        SET(checked, GET_INDEX(*it));
        find(map, *it, goal, checked, found);
    }
}

bool can_map(std::unordered_map<char, std::unordered_set<char>> &map, char a, char b)
{
    if (a == b) return true;
    int checked = 1 << (a - 'a');
    bool found = false;
    find(map, a, b, checked, found);
    return found;
}

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);

    std::unordered_map<char, std::unordered_set<char>> char_map;
    while(m--)
    {
        char a[2], b[2];
        scanf("%s %s", a, b);
        char_map[a[0]].insert(b[0]);
    }

    while(n--)
    {
        char buffer1[51], buffer2[51];
        scanf("%s %s", buffer1, buffer2);

        size_t len = strlen(buffer1);
        if (len != strlen(buffer2))
        {
            printf("no\n");
            continue;
        }

        bool equal = true;
        for (int i = 0; i < len; i++)
        {
            if (!can_map(char_map, buffer1[i], buffer2[i]))
            {
                equal = false;
                break;
            }
        }
        printf(equal ? "yes\n" : "no\n");
    }

    return 0;
}