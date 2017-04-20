#include <unordered_set>
#include <cstring>
#include "stdio.h"

#define ADD "entry"
#define IN "entered"
#define OUT "exited"
#define ANOMALY "(ANOMALY)"

int main()
{
    int n;
    scanf("%d", &n);
    char command[6], name[21];
    std::string _name;
    std::unordered_set<std::string> _set;

    while (n-- > 0)
    {
        scanf("%s %s", command, name);
        _name = std::string(name);

        if (!strcmp(ADD, command))
        {
            if (_set.find(_name) != _set.end()) printf("%s %s %s\n", name, IN, ANOMALY);
            else
            {
                _set.insert(_name);
                printf("%s %s\n", name, IN);
            }
        }
        else
        {
            if (_set.find(_name) != _set.end())
            {
                printf("%s %s\n", name, OUT);
                _set.erase(_name);
            }
            else
            {
                printf("%s %s %s\n", name, OUT, ANOMALY);
            }
        }
    }

    return 0;
}